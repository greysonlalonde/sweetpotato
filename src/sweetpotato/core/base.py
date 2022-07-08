"""Core functionality of React Native components."""
import re
from typing import Optional, Union, ClassVar

from sweetpotato.config import settings
from sweetpotato.core import ThreadSafe
from sweetpotato.core.protocols import VisitorType, ComponentVar, CompositeVar


class DOM(metaclass=ThreadSafe):
    """Mimics the document object model tree."""

    def __init__(self, graph_dict=None):
        """initializes a graph object If no dictionary or None is given, an empty dictionary will be used."""
        if not graph_dict:
            graph_dict = {}
        self.graph_dict = graph_dict

    def add_node(self, component) -> None:
        """Adds a component node to dict."""
        if component.parent not in self.graph_dict:
            self.graph_dict[component.parent] = {
                "imports": {},
                "functions": [],
                "state": {},
                "variables": [],
            }
        if component.package not in self.graph_dict[component.parent]["imports"]:
            self.graph_dict[component.parent]["imports"][component.package] = set()
        self.graph_dict[component.parent]["imports"][component.package].add(
            component.import_name,
        )
        self.graph_dict[component.parent]["variables"].append(component.variables)
        self.graph_dict[component.parent]["children"] = component


class MetaComponent(type):
    """Base React Native component metaclass for the Component class.

    Note:
        The :class:`~sweetpotato.core.base.MetaComponent` metaclass sets attributes for
        all components, including user-defined ones.
    """

    __registry = set()

    def __call__(cls, *args, **kwargs) -> None:
        if cls.__name__ not in MetaComponent.__registry:
            cls.name = MetaComponent.__set_name(cls.__name__)
            cls.import_name = cls.__set_import(cls.__name__)
            cls.package = MetaComponent.__set_package(cls.import_name, cls.__dict__)
            cls.props = MetaComponent.__set_props(cls.import_name, cls.__dict__)
            MetaComponent.__registry.add(cls.__name__)
        if set(kwargs.keys()).difference(cls.props):
            attributes = ", ".join(set(kwargs.keys()).difference(cls.props))
            raise AttributeError(
                f"Component {cls.import_name} does not have attribute(s): {attributes}"
            )
        return super().__call__(*args, **kwargs)

    @staticmethod
    def __set_import(name: str) -> str:
        """Sets React Native :attr`~sweetpotato.core.base.Component.import_name` for component.

        Args:
            name (str): React Native component import name.

        Returns:
            String representation of React Native import name for
            :class:`~sweetpotato.core.base.Component` and :class:`~sweetpotato.core.base.Composite`
        """
        return (
            name
            if name not in settings.REPLACE_COMPONENTS
            else settings.REPLACE_COMPONENTS.get(name).get("import")
        )

    @staticmethod
    def __set_name(name: str) -> str:
        """Sets React Native :attr`~sweetpotato.core.base.Component.name` for component.

        Args:
            name (str): React Native component name.

        Returns:
            String representation of React Native name for
            :class:`~sweetpotato.core.base.Component` and :class:`~sweetpotato.core.base.Composite`.
        """
        return (
            name
            if name not in settings.REPLACE_COMPONENTS
            else settings.REPLACE_COMPONENTS.get(name, name).get("name", name)
        )

    @staticmethod
    def __set_package(import_name: str, cls_dict: dict) -> str:
        """Sets React Native :attr`~sweetpotato.core.base.Component.package` for component.

        Args:
            import_name (str): React Native component name.
            cls_dict (dict): Contains :class:`sweetpotato.core.base.Component` attributes.

        Returns:
            String representation of React Native package for
            :class:`~sweetpotato.core.base.Component` and :class:`~sweetpotato.core.base.Composite`.
        """
        package = ".".join(cls_dict["__module__"].split(".")[1:2])
        return (
            settings.IMPORTS.get(package)
            if import_name not in settings.REPLACE_COMPONENTS
            else settings.REPLACE_COMPONENTS.get(import_name).get(
                "package", import_name
            )
        )

    @staticmethod
    def __set_props(name: str, cls_dict: dict) -> dict:
        """Imports and sets attribute :attr`~sweetpotato.core.base.Component._props` for all subclasses.
        Args:
            name (str): React Native component name.
            cls_dict (dict): Contains :class:`~sweetpotato.core.base.Component` attributes.
        Returns:
            Dictionary of props from :mod:`sweetpotato.props`.
        """
        package = ".".join(cls_dict["__module__"].split(".")[:2])
        props = f'{"_".join(re.findall("[A-Z][^A-Z]*", name)).upper()}_PROPS'
        pack = package.split(".")
        pack.insert(1, "props")
        package = f'{".".join(pack[:2])}.{pack[-1]}_props'
        return getattr(__import__(package, fromlist=[props]), props)


class Component(metaclass=MetaComponent):
    """Base React Native component with MetaComponent metaclass.

    Keyword Args:
        children (str, optional): Inner content for component.

    Attributes:
        _children (str, optional): Inner content for component.
        _attrs (dict): String of given attributes for component.

    Example:
        ``component = Component(children="foo")``
    """

    is_composite: ClassVar[bool] = False

    def __init__(
        self, children: Optional[str] = None, variables=None, **kwargs
    ) -> None:
        self.attrs = self.render_attrs(kwargs)
        self._children = children
        self.variables = variables if variables else ""
        self.parent = settings.APP_COMPONENT

    @property
    def children(self) -> Optional[str]:
        """Children."""
        return self._children

    def register(self, visitor: VisitorType) -> None:
        """Registers a specified visitor with component.

        Args:
            visitor (Visitor): Visitor.

        Returns:
            None
        """
        visitor.accept(self)

    @staticmethod
    def render_attrs(attrs: dict[str, str]) -> str:
        """Formats attribute to React Native friendly representation.

        Args:
            attrs (dict): Dictionary of allowed attributes specified in component props.

        Returns:
            str: String representation of dictionary.
        """
        return "".join([f" {k}={'{'}{v}{'}'}" for k, v in attrs.items()])

    def __repr__(self) -> str:
        if self._children:
            return f"<{self.name} {self.attrs}>{self.children}</{self.name}>"
        return f"<{self.name} {self.attrs}/>"


class Composite(Component):
    """Base React Native component with MetaComponent metaclass.

    Keyword Args:
        children (list, optional): Inner content for component.

    Attributes:
        _children (list, optional): Inner content for component.
        _variables (set, optional): Contains variables (if any) belonging to given component.
        _state (dict, optional): Dictionary of allowed state values for component.

    Example:
        ``composite = Composite(children=[])``
    """

    is_composite: ClassVar[bool] = True
    is_root: ClassVar[bool] = False

    def __init__(
        self,
        children: Optional[list[Union[ComponentVar, CompositeVar]]] = None,
        variables: Optional[list] = None,
        state: Optional[dict] = None,
        **kwargs,
    ) -> None:
        super().__init__(**kwargs)
        self._children = children if children else []
        self._variables = variables if variables else []
        self._state = state if state else {}

    @property
    def children(self) -> str:
        """Children."""
        return "".join(map(repr, self._children))

    def register(self, visitor) -> None:
        """Registers a specified visitor with component and child components.

        Args:
            visitor (Visitor): Visitor.

        Returns:
            None
        """
        for child in self._children:
            child.register(visitor)
        super().register(visitor)

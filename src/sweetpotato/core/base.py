"""Core functionality of React Native class based components."""
import re
from typing import Optional, Union

from sweetpotato.config import settings
from sweetpotato.core import ThreadSafe
from sweetpotato.core.protocols import RendererType, ComponentVar, CompositeVar


class DOM(metaclass=ThreadSafe):
    """Mimics the document object model tree."""

    def __init__(self, graph_dict: Optional[dict] = None) -> None:
        if not graph_dict:
            graph_dict = {}
        self.graph_dict = graph_dict

    @property
    def component(self) -> str:
        """Returns string representation of main app components."""
        return self.graph_dict[settings.APP_COMPONENT]["children"]

    def add_node(self, component: CompositeVar) -> None:
        """Adds a component node to dict.

        Args:
            component: Composite component to be added on tree.
        """
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
        if component.is_composite and component.is_root:
            self.graph_dict[component.parent]["functions"].append(
                "\n".join(component._functions)
            )


class MetaComponent(type):
    """Base React Native component metaclass for the Component class.

    Note:
        The :class:`~sweetpotato.core.base.MetaComponent` metaclass sets attributes for
        all components, including user-defined ones.
    """

    __registry: set = set()

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
            name: React Native component import name.

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
            name: React Native component name.

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
            import_name: React Native component name.
            cls_dict: Contains :class:`sweetpotato.core.base.Component` attributes.

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
        """Imports and sets attribute props for all subclasses.
        Args:
            name: React Native component name.
            cls_dict: Contains :class:`~sweetpotato.core.base.Component` attributes.
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

    Args:
        children: Inner content for component.
        variables: Contains variables (if any) belonging to given component.
        kwargs: Arbitrary keyword arguments.

    Attributes:
        _children: Inner content for component.
        attrs: String of given attributes for component.
        variables: Contains variables (if any) belonging to given component.
        parent: Name of parent component, defaults to `'App'`
        name: Name of component, set in MetaComponent.

    Example:
        ``component = Component(children="foo")``
    """

    is_composite: bool = False  #: Indicates whether component may have inner content.

    def __init__(
        self, children: Optional[str] = None, variables: Optional[str] = None, **kwargs
    ) -> None:
        self.attrs = self.render_attrs(kwargs)
        self._children = children
        self.variables = variables if variables else ""
        self.parent = settings.APP_COMPONENT

    @property
    def children(self) -> Optional[str]:
        """Property returning inner content."""
        return self._children

    def register(self, renderer: RendererType) -> None:
        """Registers a specified visitor with component.

        Args:
            renderer: Renderer.
        """
        renderer.accept(self)

    @staticmethod
    def render_attrs(attrs: dict[str, str]) -> str:
        """Formats attribute to React Native friendly representation.

        Args:
            attrs: Dictionary of allowed attributes specified in component props.

        Returns:
            String representation of dictionary.
        """
        return "".join([f" {k}={'{'}{v}{'}'}" for k, v in attrs.items()])

    def __repr__(self) -> str:
        if self._children:
            return f"<{self.name} {self.attrs}>{self.children}</{self.name}>"
        return f"<{self.name} {self.attrs}/>"


class Composite(Component):
    """Base React Native component with MetaComponent metaclass.

    Args:
        children: Inner content for component.
        variables: Contains variables (if any) belonging to given component.
        state: Dictionary of allowed state values for component.
        functions: Functions for component, passed to top level component.
        kwargs: Arbitrary keyword arguments.

    Attributes:
        _children: Inner content for component.
        _variables: Contains variables (if any) belonging to given component.
        _state: Dictionary of allowed state values for component.
        _functions: Functions for component, passed to top level component.

    Example:
        ``composite = Composite(children=[])``
    """

    is_composite: bool = True  #: Indicates whether component may have inner components.
    is_root: bool = False  #: Indicates whether component is a top level component.

    def __init__(
        self,
        children: Optional[list[Union[ComponentVar, CompositeVar]]] = None,
        variables: Optional[list[str]] = None,
        state: Optional[dict[str, str]] = None,
        functions: Optional[list[str]] = None,
        **kwargs,
    ) -> None:
        super().__init__(**kwargs)
        self._children = children if children else []
        self._variables = variables if variables else []
        self._functions = functions if functions else []
        self._state = state if state else {}

    @property
    def children(self) -> str:
        """Property returning a string rendition of child components"""
        return "".join(map(repr, self._children))

    def register(self, renderer: RendererType) -> None:
        """Registers a specified renderer with component and child components.

        Args:
            renderer (Renderer): Renderer.
        """
        for child in self._children:
            child.register(renderer)
        super().register(renderer)

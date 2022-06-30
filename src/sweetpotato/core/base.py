import re
from typing import Union, Optional, List

from sweetpotato.config import settings
from sweetpotato.core.exceptions import AttrError


def _set_props(name: str, cls_dict: dict) -> dict:
    """Imports and sets attribute :attr`~sweetpotato.core.base.Component._props` for all subclasses.

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


def _set_package(import_name: str, cls_dict: dict) -> str:
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
        else settings.REPLACE_COMPONENTS.get(import_name).get("package", import_name)
    )


def _set_name(name: str) -> str:
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


def _set_import(name: str) -> str:
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
        else settings.REPLACE_COMPONENTS.get(name, name).get("import", name)
    )


class MetaComponent(type):
    """Base React Native component metaclass for the Component class.
    Note:
        The :class:`~sweetpotato.core.base.MetaComponent` metaclass sets attributes for
        all components, including user-defined ones.

    Todo:
        * Can likely refactor to using `import_name` attr and removing `name`
    """
    __registry = set()

    def __call__(cls, *args, **kwargs) -> None:
        if cls.__name__ not in MetaComponent.__registry:
            cls.name = _set_name(cls.__name__)
            cls.import_name = _set_import(cls.__name__)
            cls.package = _set_package(cls.import_name, cls.__dict__)
            cls._props = _set_props(cls.name, cls.__dict__)
            cls.__registry.add(cls.name)
        if set(kwargs.keys()).difference(cls._props):
            attributes = "".join(set(kwargs.keys()).difference(cls._props))
            raise AttrError(key=attributes, name=cls.name)
        return super().__call__(*args, **kwargs)


class Component(metaclass=MetaComponent):
    """Base React Native component with MetaComponent metaclass.

    Keyword Args:
        children (str, optional): Inner content for component.

    Attributes:
        children (str, optional): Inner content for component.
        variables (set): Contains variables (if any) belonging to given component.
        attrs (dict): String of given attributes for component.

    Example:
        ``component = Component(children="foo")``
    """
    is_screen: bool = False
    is_root: bool = False
    is_composite: bool = False
    package: str = "components"

    def __init__(
            self, children: Optional[Union[int, str]] = None, variables=None, **kwargs
    ) -> None:
        if variables is None:
            variables = []
        self._rendition = None
        self.variables = variables
        self.attrs = kwargs
        self.children = children
        self.parent = settings.APP_COMPONENT

    def register(self, visitor) -> None:
        """Registers a specified visitor with component.

        Args:
            visitor (Visitor): Visitor.

        Returns:
            None
        """
        visitor.accept(self)

    @property
    def rendition(self) -> Optional[str]:
        """Placeholder for component rendition, set by visitor.

        Returns:
            str: Rendition of component.
        """
        return self._rendition

    @rendition.setter
    def rendition(self, rendition) -> None:
        self._rendition = rendition


class Composite(Component):
    is_composite: bool = True

    def __init__(
            self, children: Optional[Union[List, "Composite"]] = None, **kwargs
    ) -> None:
        super().__init__(**kwargs)
        self.children = children if children else []

    def register(self, visitor) -> None:
        """Registers a specified visitor with component and child components.

        Args:
            visitor (Visitor): Visitor.

        Returns:
            None
        """
        for child in self.children:
            child.register(visitor)
        super().register(visitor)

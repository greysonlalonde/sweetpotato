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


def _set_package(name: str, cls_dict: dict) -> str:
    """Sets component React Native package.

    Args:
        name: React Native component name.
        cls_dict: Contains :class:`sweetpotato.core.base.Component` attributes.

    Returns:
        String representation of React Native package for given :class:`sweetpotato.core.base.Component`.
    """
    package = ".".join(cls_dict["__module__"].split(".")[1:2])
    return (
        settings.IMPORTS.get(package)
        if name not in settings.REPLACE_COMPONENTS
        else settings.REPLACE_COMPONENTS.get(name, name).get("package", name)
    )


def _set_name(name: str):
    return (
        name
        if name not in settings.REPLACE_COMPONENTS
        else settings.REPLACE_COMPONENTS.get(name, name).get("name", name)
    )


def _set_component_name(name: str):
    return (
        name
        if name not in settings.REPLACE_COMPONENTS
        else settings.REPLACE_COMPONENTS.get(name, name).get("component_name", name)
    )


def _set_import(name: str):
    return (
        name
        if name not in settings.REPLACE_COMPONENTS
        else settings.REPLACE_COMPONENTS.get(name, name).get("import", name)
    )


class MetaComponent(type):
    __registry = set()

    def __call__(cls, *args, **kwargs) -> None:
        if cls.__name__ not in MetaComponent.__registry:
            cls.name = _set_name(cls.__name__)
            cls.component_name = _set_component_name(cls.__name__)
            cls.import_name = _set_import(cls.__name__)
            cls._props = _set_props(cls.name, cls.__dict__)
            cls._package = _set_package(cls.name, cls.__dict__)
            cls.__registry.add(cls.name)
        if set(kwargs.keys()).difference(cls._props):
            attributes = "".join(set(kwargs.keys()).difference(cls._props))
            raise AttrError(key=attributes, name=cls.name)
        return super().__call__(*args, **kwargs)


class Component(metaclass=MetaComponent):
    is_screen: bool = False
    is_root: bool = False
    is_composite: bool = False
    package: str = "components"

    def __init__(self, children: Optional[Union[int, str]] = None, **kwargs) -> None:
        self._rendition = None
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

    def register(self, visitor):
        """Registers a specified visitor with component and child components.

        Args:
            visitor (Visitor): Visitor.

        Returns:
            None
        """
        for child in self.children:
            child.register(visitor)
        super().register(visitor)

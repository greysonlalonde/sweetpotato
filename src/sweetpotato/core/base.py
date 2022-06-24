import re
from typing import Union, Optional
from sweetpotato.config import settings
from sweetpotato.core.exceptions import AttrError


def set_props(name: str, cls_dict: dict) -> dict:
    """Imports and sets attribute :attr`~sweetpotato.core.base.Component._props` for all subclasses.

    Args:
        name: React Native component name.
        cls_dict: Contains :class:`~sweetpotato.core.base.Component` attributes.

    Returns:
        Dictionary of props from :mod:`sweetpotato.props`.
    """
    if name == settings.APP_COMPONENT:
        return settings.APP_PROPS
    package = ".".join(cls_dict["__module__"].split(".")[:2])
    props = f'{"_".join(re.findall("[A-Z][^A-Z]*", name)).upper()}_PROPS'
    pack = package.split(".")
    pack.insert(1, "props")
    package = f'{".".join(pack[:2])}.{pack[-1]}_props'
    return getattr(__import__(package, fromlist=[props]), props)


def set_package(name: str, cls_dict: dict) -> str:
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
        else settings.REPLACE_COMPONENTS.get(name)["package"]
    )


class MetaComponent(type):
    __registry = set()

    def __call__(cls, *args, **kwargs) -> None:
        if cls.__name__ not in MetaComponent.__registry:
            cls.name = cls.__name__
            cls.__registry.add(cls.name)
            cls._props = set_props(cls.name, cls.__dict__)
            cls._package = set_package(cls.name, cls.__dict__)
        if set(kwargs.keys()).difference(cls._props):
            attributes = "".join(set(kwargs.keys()).difference(cls._props))
            raise AttrError(key=attributes, name=cls.name)
        return super().__call__(*args, **kwargs)


class Component(metaclass=MetaComponent):
    is_composite: bool = False
    package: str = "components"

    def __init__(
        self, children: Optional[Union[int, str]] = None, *args, **kwargs
    ) -> None:
        self.children = children
        self.parent = None

    def register(self, visitor) -> list:
        results = visitor.accept(self)
        return results


class Composite(Component):
    is_composite: bool = True

    def __init__(self, **kwargs) -> None:
        super().__init__(
            children=kwargs.pop("children") if kwargs.get("children") else [], **kwargs
        )
        for child in self.children:
            child.parent = self

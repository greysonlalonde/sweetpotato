"""Base React Native component implementation.

"""

import re
from typing import Union, Optional, Type

from sweetpotato.config import settings
from sweetpotato.core.exceptions import AttrError


class MetaComponent(type):
    """Base React Native component metaclass for the Component class.

    Note:
        The :class:`~sweetpotato.core.base.MetaComponent` metaclass sets attributes for
        all components.

    Todo:
       Replaces occurrences of ``object`` type checking with typing.Generic or typing.Protocol
    """

    def __new__(mcs, name: str, bases: tuple, cls_dict: dict) -> Union[object, None]:
        # Initialize subclasses, exclude :class:`~sweetpotato.core.base.MetaComponent`.
        obj = super().__new__(mcs, name, bases, cls_dict)
        return (
            obj
            if not list(map(lambda x: isinstance(x, MetaComponent), bases))
            else obj.set_component(obj, name, cls_dict)
        )

    @classmethod
    def set_component(mcs, obj: object, name: str, cls_dict: dict) -> object:
        """Initializes subclass component and sets methods/attributes.

        Args:
            obj: Base Component object.
            name: React Native component name.
            cls_dict: Contains :class:`sweetpotato.core.base.Component` attributes.

        Returns:
            :class:`sweetpotato.core.base.Component` with altered/added attrs.
        """
        cls_dict = mcs.set_module(name, cls_dict)
        obj._package = mcs.set_package(name, cls_dict)
        obj._name = mcs.set_component_name(name)
        obj._functions = mcs.set_functions(obj._name)
        obj._type = mcs.set_type(name)
        obj._react_component = mcs.set_component_name(obj._name)
        obj._props = mcs.set_props(obj._name, cls_dict)
        return obj

    @classmethod
    def set_functions(mcs, name: str) -> str:
        """Sets functions and authentication functions (if using authentication) for subclass.

        Args:
            name: React Native component name.
        """
        component_functions = settings.FUNCTIONS.get(name, "")
        return (
            component_functions + settings.AUTH_FUNCTIONS.get(name, "")
            if settings.USE_AUTHENTICATION
            else component_functions
        )

    @classmethod
    def set_props(mcs, name: str, cls_dict: dict) -> dict:
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

    @classmethod
    def set_type(mcs, name: str) -> str:
        """Sets the component type.

        Args:
            name: React Native component name.

        Returns:
            Modified :class:`~sweetpotato.core.base.Component` type.
        """
        return list(re.findall("[A-Z][^A-Z]*", name))[0]

    @classmethod
    def set_package(mcs, name: str, cls_dict: dict) -> str:
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

    @classmethod
    def set_module(mcs, name: str, cls_dict: dict) -> dict:
        """Sets react module for subclass.

        Args:
            name: React Native component name.
            cls_dict: Contains :class:`sweetpotato.core.base.Component` attributes.

        Returns:
            Attribute dictionary for given :class:`sweetpotato.core.base.Component`.
        """
        if settings.USE_UI_KITTEN:
            cls_dict["__module__"] = (
                "sweetpotato.ui_kitten"
                if name in settings.UI_KITTEN_REPLACEMENTS
                else cls_dict["__module__"]
            )
        return cls_dict

    @classmethod
    def set_component_name(mcs, name: str) -> str:
        """Sets component name for given class.

        Args:
            name: React Native component name.

        Returns:
            Modified :class:`sweetpotato.core.base.Component` name.
        """
        return (
            name
            if name not in settings.REPLACE_COMPONENTS
            else settings.REPLACE_COMPONENTS.get(name)["import"]
        )


def metaclass(meta: Type[MetaComponent]):
    """Decorator for the metaclass.

    ``Component(metaclass=MetaComponent)`` looked funky to me.

    Args:
        meta: Any metaclass to be taken by a class.

    Returns:
        :class:`sweetpotato.core.base.Component` with manipulated attrs.
    """

    def wrapper(cls):

        __name = str(cls.__name__)
        __bases = tuple(cls.__bases__)
        __dict = dict(cls.__dict__)
        for __slot in __dict.get("__slots__", tuple()):
            __dict.pop(__slot, None)
        __dict["__metaclass__"] = meta
        return meta(__name, __bases, __dict)

    return wrapper


@metaclass(MetaComponent)
class Component:
    """Base React Native component with MetaComponent metaclass.

    Keyword Args:
        children: List of child components.

    Attributes:
        _imports (dict): Contains all React Native based imports for given component.
        _children (list): Contains all child components to be written.
        _variables (set): Contains variables (if any) belonging to given component.
        _attrs (str): String of given attributes for component.

    Example:
        ``component = Component(children=[])``

    Todo:
        Need to refactor and migrate multiple attributes to
        :class:`sweetpotato.navigation.Screen`. as they
        introduce leaky abstraction.
    """

    def __init__(self, children: Optional[list] = None, **kwargs) -> None:
        self._imports = {}
        self._children = children
        self._variables = set()
        self._attrs = self.format_attr(**kwargs)

    def write_component(self) -> str:
        """Render React Native friendly string representation of component.

        Returns:
            React Native friendly string representation.
        """
        if self._children:
            children = "".join([child.write_component() for child in self._children])
            return (
                f"<{self._react_component} {self._attrs if self._attrs else ''}>"
                f"{children}\n</{self._react_component}>"
            )

        return f"<{self._react_component} {self._attrs}/>"

    def write_functions(self) -> str:
        """Gathers functions from component and child components.

        Returns:
            String representation of component functions.
        """
        functions = ""
        if self._children:
            functions += "".join([child.write_functions() for child in self._children])
        return functions + self._functions

    def write_import(self) -> dict:
        """Gathers child components and self imports.

        Returns:
            All child imports.
        """
        self_imports = {}
        if self._children:
            print(self)
            print(self._children)
            child_imports = [child.write_import() for child in self._children]
            for imports in child_imports:
                for key, value in imports.items():
                    if key not in self_imports:
                        self_imports[key] = set()
                    for val in value:
                        self_imports[key].add(val)

        if self._package not in self_imports:
            self_imports[self._package] = set()
        self_imports[self._package].add(self._react_component)
        return self_imports

    def write_variables(self) -> str:
        """Writes const variables (if present) to App.js file.

        Returns:
            String representation of variables for component.
        """
        return "".join(list(self._variables))

    def format_attr_dict(self, key: str, attr: str) -> Union[dict, str]:
        """Formats attribute to React Native friendly representation.

        Args:
            key: key for given attribute.
            attr: attribute for given key.

        Returns:
            React Native friendly representation of attribute.

        Raises:
            :exc:`sweetpotato.core.exceptions.AttrError`
        """

        if key not in self._props:
            raise AttrError(key, self._name)

        return (
            attr if attr in settings.DEFAULT_EXPORTS.values() else "{" + str(attr) + "}"
        )

    def format_attr(self, **attr: Union[dict, str]) -> str:
        """Formats attribute to react-native friendly representation.

        Args:
            attr: Given attributes for component.

        Returns:
            React Native friendly representation of attribute.

        Todo:
            Remove hard-coded list.
        """
        attrs = ""
        for key, value in attr.items():
            if key not in self._props:
                raise AttrError(key, self._name)
            if type(value) == str and key not in settings.REPLACE_ATTRS:
                value = "'" + str(value) + "'"
            if key in settings.REPLACE_ATTRS and key not in [
                "onChangeText",
                "onPress",
                "value",
                "placeholder",
                "secureTextEntry",
            ]:
                value = settings.REPLACE_ATTRS[key][value]
            attrs += f" {key}=" + "{" + str(value) + "}"
        return attrs

    def __repr__(self) -> str:
        """Custom __repr__ method to show component.

        Returns:
             React Native friendly representation of component.
        """
        return self.write_component()

"""
Todo:
    * Add docstrings for all classes & methods.
    * Add typing.
"""
from abc import ABC, abstractmethod
from typing import Union

from sweetpotato.core import ThreadSafe
from sweetpotato.core.protocols import Component, Composite


class Storage(metaclass=ThreadSafe):
    """Provides storage for app internals."""

    internals = {}


class Visitor(ABC):
    """Interface for visitors."""

    @classmethod
    @abstractmethod
    def accept(cls, obj: Union[Component, Composite]) -> None:
        """Accepts a component and performs an action.

        Args:
            obj (Component): Component object.

        Returns:
            None
        """
        raise NotImplementedError


class ApplicationRenderer(Visitor):
    rendered = set()

    @classmethod
    def accept(cls, obj: Composite) -> None:
        cls.render_imports(obj)
        cls.render_variables(obj)
        cls.render_functions(obj)

    @classmethod
    def render_imports(cls, obj: Composite):
        if obj.is_root:
            formatted = Storage.internals[obj.parent].pop("imports")
            Storage.internals[obj.parent]["imports"] = cls.format_imports(formatted)

    @classmethod
    def format_imports(cls, imports: dict[str, str]) -> str:
        """Formats import dictionary to React Native friendly representation.

        Returns:
            String representation of all imports.
        """
        import_str = ""
        for k, v in imports.items():
            print(k, v)
            import_str += f'import {v} from "{k}";\n'.replace("'", "")

        return import_str

    @classmethod
    def render_variables(cls, obj: Union[Component, Composite]) -> None:
        variables = "".join([f"\n{var};" for var in obj.variables])
        Storage.internals[obj.parent]["variables"].append(variables)

    @classmethod
    def render_functions(cls, obj: Union[Component, Composite]) -> None:
        # if obj.is_screen:
        #     functions = "".join([f"\n{function};" for function in obj.functions])
        #     Storage.internals[obj.import_name]["functions"].append(functions)
        ...


class ComponentRenderer(Visitor):
    """Accumulates react-native friendly string representations of components."""

    @classmethod
    def accept(cls, obj: Union[Component, Composite]) -> None:
        """Accepts a component and adds a .js compatible rendition.

        Args:
            obj (Component): Component object.

        Returns:
            None
        """

        # obj.rendition = cls.render_component(obj)
        Storage.internals[obj.parent] = {
            "component": str(obj),
            "imports": {},
            "variables": [],
            "functions": [],
        }


class ImportRenderer(Visitor):
    """Accumulates component imports per screen."""

    @classmethod
    def accept(cls, obj: Union[Component, Composite]) -> None:
        """Accepts a component and records component imports.

        Args:
            obj (`Component`): Component object.

        Returns:
            None
        """
        if obj.parent not in Storage.internals:
            Storage.internals[obj.parent] = {"imports": {}}
        cls.add_import(obj)

    @classmethod
    def add_import(cls, obj: Union[Component, Composite]) -> None:
        """Adds import dictionary to Storage object.

        Returns:
            String representation of all imports.
        """

        if obj.is_screen:
            Storage.internals[obj.parent]["imports"][obj.package] = obj.import_name
        else:
            if obj.package not in Storage.internals[obj.parent]["imports"]:
                Storage.internals[obj.parent]["imports"][obj.package] = set()
            Storage.internals[obj.parent]["imports"][obj.package].add(obj.import_name)

"""
Todo:
    * Add docstrings for all classes & methods.
    * Add typing.
"""
from abc import ABC, abstractmethod
from typing import Union

from sweetpotato.core import ThreadSafe
from sweetpotato.core.protocols import Component, Composite, Screen


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
            obj (Component | Composite): Component instance.

        Returns:
            None
        """
        raise NotImplementedError


class ApplicationRenderer(Visitor):
    """Accepts a top level component and performs all rendering."""

    rendered = set()

    @classmethod
    def accept(cls, obj: Union[Composite, Screen]) -> None:
        """Accepts a component and performs ....

        Args:
            obj (Composite | Screen): Component object.

        Returns:
            None
        """
        cls._render_imports(obj)
        cls._render_variables(obj)
        cls._render_state(obj)
        cls._render_functions(obj)

    @classmethod
    def _render_imports(cls, obj: Composite) -> None:
        """Adds imports to storage instance in a React Native acceptable format.

        Args:
            obj (Composite): ...

        Returns:
            None
        """
        if obj.is_root:
            formatted = Storage.internals[obj.parent].pop("imports")
            Storage.internals[obj.parent]["imports"] = cls.__format_imports(formatted)

    @staticmethod
    def __format_imports(imports: dict[str, str]) -> str:
        """Formats import dictionary to React Native friendly representation.

        Args:
            imports (dict): Dictionary of imports in a package: import fashion.

        Returns:
            str: String representation of all imports.
        """
        import_str = ""
        for k, v in imports.items():
            import_str += f'import {v} from "{k}";\n'.replace("'", "")

        return import_str

    @classmethod
    def _render_variables(cls, obj: Union[Component, Composite]) -> None:
        """Adds variables to storage instance in a React Native acceptable format.

        Args:
            obj (Component | Composite): ...

        Returns:
            None
        """
        variables = "".join([f"\n{var};" for var in obj.variables])
        Storage.internals[obj.parent]["variables"].append(variables)

    @classmethod
    def _render_state(cls, obj: Screen) -> None:
        """Adds state to storage instance in a React Native acceptable format.

        Args:
            obj (Screen): ...

        Returns:
            None
        """
        if obj.is_screen:
            state = ",".join([f"\n{key}: {value}" for key, value in obj.state.items()])
            Storage.internals[obj.parent]["state"] = state

    @classmethod
    def _render_functions(cls, obj: Screen) -> None:
        """Adds functions to storage instance in a React Native acceptable format.

        Args:
            obj (Screen): ...

        Returns:
            None
        """
        if obj.is_screen:
            functions = "".join([f"\n{function};" for function in obj.functions])
            Storage.internals[obj.import_name]["functions"].append(functions)


class ComponentRenderer(Visitor):
    """Accumulates react-native friendly string representations of components."""

    @classmethod
    def accept(cls, obj: Union[Component, Composite]) -> None:
        """Accepts a component and adds a .js compatible rendition.

        Args:
            obj (Component | Composite): Component instance.

        Returns:
            None
        """

        Storage.internals[obj.parent] = {
            "component": str(obj),
            "imports": {},
            "variables": [],
            "functions": [],
            "state": [],
        }


class ImportRenderer(Visitor):
    """Accumulates component imports per screen."""

    @classmethod
    def accept(cls, obj: Union[Component, Composite]) -> None:
        """Accepts a component and records component imports.

        Args:
            obj (Component | Composite): Component instance.

        Returns:
            None
        """
        if obj.parent not in Storage.internals:
            Storage.internals[obj.parent] = {"imports": {}}
        cls.__add_import(obj)

    @classmethod
    def __add_import(cls, obj: Union[Component, Composite]) -> None:
        """Adds import dictionary to Storage object.

        Args:
            obj (Component | Composite): Component instance.

        Returns:
            None
        """

        if obj.is_screen:
            Storage.internals[obj.parent]["imports"][obj.package] = obj.import_name
        else:
            if obj.package not in Storage.internals[obj.parent]["imports"]:
                Storage.internals[obj.parent]["imports"][obj.package] = set()
            Storage.internals[obj.parent]["imports"][obj.package].add(obj.import_name)

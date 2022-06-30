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

    @classmethod
    def render_application(cls, obj: Composite):
        ...

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
            import_str += f'import {v} from "{k}";\n'.replace("'", "")

        return import_str

    @classmethod
    def render_variables(cls, obj: Union[Component, Composite]) -> None:
        Storage.internals[obj.parent]["variables"].append("".join(obj.variables))


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

        obj.rendition = cls.render_component(obj)
        Storage.internals[obj.parent] = {
            "component": obj.rendition,
            "imports": {},
            "variables": [],
        }

    @classmethod
    def render_children(cls, obj: Union[Component, Composite]) -> str:
        """Returns component inner content in a compatible format.

        Args:
            obj (Component): Component type.

        Returns:
            str: Component children in a string format.
        """
        return (
            "".join(map(lambda child: child.rendition, obj.children))
            if obj.is_composite
            else obj.children
        )

    @classmethod
    def render_component(cls, obj: Union[Component, Composite]) -> str:
        """Render React Native friendly string representation of component.

        Args:
            obj (Component): Component or Composite object.

        Returns:
            str: React Native friendly string representation.
        """
        attrs = cls.render_attrs(obj.attrs)
        if obj.children and not obj.is_screen:
            return f"\n<{obj.name}{attrs}>{cls.render_children(obj)}</{obj.name}>"
        return f"\n<{obj.name} {attrs}/>\n"

    @classmethod
    def render_attrs(cls, attrs: dict[str, str]) -> str:
        """Formats attribute to React Native friendly representation.

        Args:
            attrs (dict): Dictionary of allowed attributes specified in component props.

        Returns:
            str: String representation of dictionary.
        """
        return "".join([f" {k}={'{'}{v}{'}'}" for k, v in attrs.items()])


class ImportRenderer(Visitor):
    """Accumulates component imports per screen."""

    @classmethod
    def accept(cls, obj: Union[Component, Composite]) -> None:
        """Accepts a component and records component imports.

        Args:
            obj (Component): Component object.

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

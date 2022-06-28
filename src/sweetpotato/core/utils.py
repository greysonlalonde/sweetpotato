from abc import ABC, abstractmethod

from sweetpotato.config import settings
from sweetpotato.core.protocols import Component


class AppProxy:
    """Provides storage for app internals."""

    internals = {}


class Visitor(ABC):
    """Interface for visitors."""

    @classmethod
    @abstractmethod
    def accept(cls, obj: Component) -> None:
        """Accepts a component and performs an action.

        Args:
            obj (Component): Component object.

        Returns:
            None
        """
        raise NotImplementedError


class Renderer(Visitor):
    """Accumulates react-native friendly string representations of components."""

    @classmethod
    def accept(cls, obj: Component) -> None:
        """Accepts a component and adds a .js compatible rendition.

        Args:
            obj (Component): Component object.

        Returns:
            None
        """

        obj.rendition = cls.render_component(obj)
        AppProxy.internals[obj.parent] = {"component": obj.rendition, "imports": {}}

    @classmethod
    def render_children(cls, obj: Component) -> str:
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
    def render_component(cls, obj: Component) -> str:
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


class Importer(Visitor):
    """Accumulates component imports per screen."""

    @classmethod
    def accept(cls, obj: Component) -> None:
        """Accepts a component and records component imports.

        Args:
            obj (Component): Component object.

        Returns:
            None
        """
        if obj.parent not in AppProxy.internals:
            obj.imports = cls.replace_import(obj)
            AppProxy.internals[obj.parent] = {"imports": {}}
        cls.add_import(obj)

    @classmethod
    def replace_import(cls, obj: Component) -> dict[str, str]:
        """Replaces package name with specified package in `default_settings.Settings`.

        Args:
            obj (Component): Component type.

        Returns:
            dict: Dictionary of key values as "component name": "component package".
        """
        return {
            obj.import_name: settings.IMPORTS.get(obj.package, obj.import_name)
            if obj.name not in settings.REPLACE_COMPONENTS
            else settings.REPLACE_COMPONENTS.get(obj.name, obj.import_name).get(
                "package", obj.import_name
            )
        }

    @classmethod
    def add_import(cls, obj: Component) -> None:
        """Adds import dictionary to AppProxy object.

        Returns:
            String representation of all imports.
        """
        obj.imports = cls.replace_import(obj)
        component, package = tuple((k, v) for k, v in obj.imports.items())[0]
        if package not in AppProxy.internals[obj.parent]["imports"]:
            AppProxy.internals[obj.parent]["imports"][package] = set()
        AppProxy.internals[obj.parent]["imports"][package].add(component)

    @classmethod
    def format_imports(cls, imports: dict[str, str]) -> str:
        """Formats import dictionary to React Native friendly representation.

        Returns:
            String representation of all imports.
        """
        import_str = ""
        for k, v in imports.items():
            left = "{"
            right = "}"
            import_str += f'import {left}{k}{right} from "{v}";\n'.replace("'", "")
        return import_str

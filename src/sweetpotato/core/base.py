"""Core functionality of React Native class based components."""
import json
from typing import Optional, Union

from sweetpotato.config import settings
from sweetpotato.core import ThreadSafe
from sweetpotato.core.protocols import (
    RendererType,
    ComponentVar,
    CompositeVar,
    CompositeType,
    ComponentType,
)


class Component:
    """Base React Native component with MetaComponent metaclass.

    Args:
        children: Inner content for component.
        variables: Contains variables (if any) belonging to given component.
        kwargs: Arbitrary keyword arguments.

    Attributes:
        _children: Inner content for component.
        _attrs: String of given attributes for component.
        _variables: Contains variables (if any) belonging to given component.
        props: Allowed props for component.
        parent: Name of parent component, defaults to `'App'`.

    Example:
        component = Component(children="foo")
    """

    package: str = "react-native"
    props: set = {}  #: Set of allowed props for component.
    is_composite: bool = False  #: Indicates whether component may have inner content.

    def __init__(
            self,
            component_name: Optional[str] = None,
            children: Optional[str] = None,
            variables: Optional[list[str]] = None,
            **kwargs,
    ) -> None:
        if set(kwargs.keys()).difference(self.props):
            attributes = ", ".join(set(kwargs.keys()).difference(self.props))
            raise AttributeError(
                f"{self.import_name} component does not have attribute(s): {attributes}"
            )
        self.component_name = (
            component_name if component_name else self._set_default_name()
        )
        self._import_name = self.__class__.__name__
        self._attrs = kwargs
        self._children = children
        self._variables = variables if variables else []
        self.parent = settings.APP_COMPONENT

    @property
    def import_name(self):
        return self._import_name

    @import_name.setter
    def import_name(self, name):
        self._import_name = name

    @property
    def children(self) -> Optional[str]:
        """Property returning inner content."""
        return self._children

    @property
    def attrs(self) -> Optional[str]:
        """Property string of given attributes for component"""
        return "".join([f" {k}={'{'}{v}{'}'}" for k, v in self._attrs.items()])

    @property
    def variables(self) -> Optional[str]:
        """Property returning string of variables (if any) belonging to given component."""
        return "\n".join(self._variables)

    def _set_default_name(self):
        return self.__class__.__name__

    def register(self, renderer: RendererType) -> None:
        """Registers a specified visitor with component.

        Args:
            renderer: Renderer.
        """
        renderer.accept(self)

    def __repr__(self) -> str:
        if self._children:
            return f"<{self.component_name} {self.attrs}>{self.children}</{self.component_name}>"
        return f"<{self.component_name} {self.attrs}/>"


class Composite(Component):
    """Base React Native component with MetaComponent metaclass.

    Args:
        children: Inner content for component.
        state: Dictionary of allowed state values for component.
        functions: Functions for component, passed to top level component.
        kwargs: Arbitrary keyword arguments.

    Attributes:
        _children: Inner content for component.
        _state: Dictionary of allowed state values for component.
        _functions: Functions for component, passed to top level component.

    Example:
        composite = Composite(children=[])
    """

    is_context: bool = False  #: Indicates whether component is a context, similar to an inline if else.
    is_composite: bool = True  #: Indicates whether component may have inner components.
    is_root: bool = False  #: Indicates whether component is a top level component.

    def __init__(
            self,
            children: Optional[list[Union[ComponentVar, CompositeVar]]] = None,
            functions: Optional[list[str]] = None,
            **kwargs,
    ) -> None:
        super().__init__(**kwargs)
        self._children = children if children else []
        self._functions = functions if functions else []

    @property
    def children(self) -> str:
        """Property returning a string rendition of child components"""
        return "".join(map(repr, self._children))

    @property
    def functions(self) -> Optional[str]:
        """Property returning string of variables (if any) belonging to given component."""
        return "".join(self._functions)

    def register(self, renderer: RendererType) -> None:
        """Registers a specified renderer with component and child components.

        Args:
            renderer (Renderer): Renderer.
        """
        for child in self._children:
            child.register(renderer)
        if not self.is_context:
            super().register(renderer)


class ComponentRegistry(metaclass=ThreadSafe):
    _registry = {}

    @classmethod
    @property
    def registry(cls):
        return cls._registry

    @classmethod
    def register(cls, component):
        if component.component_name not in cls._registry.keys():
            cls._registry[component.component_name] = component


class RootComponent(Composite):
    """Root component.

    Args:
        component_name: Name of .js class/function/const for component.
        kwargs: Arbitrary keyword arguments.

    Attributes:
        component_name: Name of .js class/function/const for component.
        import_name: Name of .js class/function/const for component import.

    """

    package_root: str = f"./{settings.SOURCE_FOLDER}/components"
    is_root: bool = True  #: Indicates whether component is a top level component.
    is_functional: bool = (
        False  #: Indicates whether component a functional or class component.
    )

    def __init__(
            self,
            state: Optional[dict[str, str]] = None,
            extra_imports: Optional[dict[str, str]] = None,
            **kwargs,
    ) -> None:
        super().__init__(**kwargs)
        self._state = state if state else {}
        self.import_name = "".join(
            [word.title() for word in self.component_name.split(" ")]
        )
        self.package = f"{self.package_root}/{self.import_name}.js"
        self._imports = {}
        self._set_parent(self._children)
        if extra_imports:
            self._imports.update(extra_imports)
        ComponentRegistry.register(self)

    @property
    def imports(self):
        import_string = ""
        for key, value in self._imports.items():
            print(key, value)
            import_string += (
                f'import {value} from "{key}";\n'.replace("'", "")
                if value
                else f'import "{key}"\n'
            )

        return import_string

    @property
    def state(self):
        return json.dumps(self._state)

    def _set_parent(self, children: list[Union[CompositeType, ComponentType]]) -> None:
        """Sets top level component as root and sets each parent to self.

        Args:
            children: List of components.
        """
        for child in children:
            child.parent = self.component_name
            if (child.is_composite and not child.is_context) or not child.is_composite:
                if child.package not in self._imports:
                    self._imports[child.package] = set()
                self._imports[child.package].add(child.import_name)
            if child.is_composite:
                self._functions.append(child.functions)
                self._variables.append(child.variables)
                self._set_parent(child._children)


class App(RootComponent):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.package = f"{settings.REACT_NATIVE_PATH}/{self.import_name}.js"

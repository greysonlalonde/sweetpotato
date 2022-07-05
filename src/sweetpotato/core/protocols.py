"""Provides custom protocols for typing.

Todo:
    * Add docstrings for all classes & methods.
    * Add typing.
"""
from typing import Protocol, Optional, Union


class Screen(Protocol):
    """Protocol for Screen class."""

    is_screen: bool
    state: dict
    functions: list
    parent: Optional[str]
    import_name: str

    def __set_parent(self) -> None:
        ...


class Component(Protocol):
    """Protocol for Component class."""

    parent: str
    attrs: Optional[dict[str, str]]
    name: str
    import_name: str
    is_composite: bool
    variables: list
    package: dict
    children: Optional[str]

    def register(self, visitor) -> None:
        """Registers given visitor with component.

        Args:
            visitor (Visitor): Visitor instance.

        Returns:
            None
        """
        ...


class Composite(Component, Protocol):
    """Protocol for Composite class."""

    parent: Optional[str]
    is_screen: bool
    is_root: bool
    children: Optional[list[Union[Component, "Composite"]]]


class Visitor(Protocol):
    """Protocol for Visitor class."""

    def accept(self, component: Union[Component, Composite]) -> None:
        """Accepts a component and performs an action.

        Args:
            component (Component | Composite): Component object.

        Returns:
            None
        """
        ...

"""
Todo:
    * Add docstrings for all classes & methods.
    * Add typing.
"""
from typing import Protocol, Optional, Union


class Screen(Protocol):
    is_screen: bool
    state: dict
    functions: list
    parent: Optional[str]
    import_name: str


class Component(Protocol):
    parent: str
    attrs: Optional[dict[str, str]]
    name: str
    import_name: str
    is_composite: bool
    variables: list
    package: dict
    children: Optional[Union[str]]

    def register(self, visitor) -> list:
        ...


class Composite(Component, Protocol):
    parent: Optional[str]
    is_screen: bool
    is_root: bool
    children: Optional[list[Union[Component, "Composite"]]]


class Visitor(Protocol):
    def accept(self, component: Union[Component, Composite]) -> None:
        """Accepts a component and performs an action.

        Args:
            component (Component): Component object.

        Returns:
            None
        """
        ...

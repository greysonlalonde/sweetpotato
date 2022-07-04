"""
Todo:
    * Add docstrings for all classes & methods.
    * Add typing.
"""
from typing import Protocol, Optional, List, Union


class Component(Protocol):
    parent: str
    attrs: Optional[dict[str, str]]
    rendition: str
    imports: dict
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
    children: Optional[List[Union[Component, "Composite"]]]


class Visitor(Protocol):
    def accept(self, component: Union[Component, Composite]) -> None:
        """Accepts a component and performs an action.

        Args:
            component (Component): Component object.

        Returns:
            None
        """
        ...

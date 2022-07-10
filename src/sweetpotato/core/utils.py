"""
Todo:
    * Can refactor away from using abstract class.
"""
from abc import ABC, abstractmethod

from sweetpotato.core.base import DOM
from sweetpotato.core.protocols import ComponentType, CompositeType


class Renderer(ABC):
    """Interface for visitors."""

    @classmethod
    @abstractmethod
    def accept(cls, obj: ComponentType | CompositeType) -> None:
        """Accepts a component and performs an action.

        Args:
            obj (Component | Composite): Component instance.

        Returns:
            None
        """
        raise NotImplementedError


class ApplicationRenderer(Renderer):
    """Accepts a top level component and performs all rendering."""

    dom = DOM()

    @classmethod
    def accept(cls, obj: CompositeType) -> None:
        """Accepts a component and performs ....

        Args:
            obj (Composite): Component object.

        Returns:
            None
        """
        cls.dom.add_node(obj)

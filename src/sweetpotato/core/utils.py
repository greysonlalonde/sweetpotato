"""
Todo:
    * Add docstrings for all classes & methods.
    * Add typing.
"""
from abc import ABC, abstractmethod
from typing import Union

from sweetpotato.core.base import DOM
from sweetpotato.core.protocols import Component, Composite, Screen


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

    dom = DOM()

    @classmethod
    def accept(cls, obj: Union[Composite, Screen]) -> None:
        """Accepts a component and performs ....

        Args:
            obj (Composite | Screen): Component object.

        Returns:
            None
        """
        cls.dom.add_node(obj)

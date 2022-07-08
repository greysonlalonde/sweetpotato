"""Provides custom protocols for typing.

Todo:
    * Add docstrings for all classes & methods.
    * Add typing.
"""
from typing import TypeVar, Type

ComponentVar = TypeVar("ComponentVar", bound="Component")
ComponentType = Type[ComponentVar]

CompositeVar = TypeVar("CompositeVar", bound="Composite")
CompositeType = Type[ComponentVar]

VisitorVar = TypeVar("VisitorVar", bound="Visitor")
VisitorType = Type[VisitorVar]

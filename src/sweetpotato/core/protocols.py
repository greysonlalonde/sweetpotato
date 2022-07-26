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

ContextWrapperVar = TypeVar("ContextWrapperVar", bound="ContextWrapper")
ContextWrapperType = Type[ContextWrapperVar]

BuildVar = TypeVar("BuildVar", bound="Build")
BuildType = Type[BuildVar]

RendererVar = TypeVar("RendererVar", bound="Renderer")
RendererType = Type[RendererVar]

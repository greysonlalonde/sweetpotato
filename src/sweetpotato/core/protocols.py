from typing import Protocol, Optional, List, Union

from sweetpotato.config import settings


class Component(Protocol):
    name: str
    parent: "Component"
    is_composite: bool = False
    is_root: bool = False
    package: dict
    children: Optional[Union[int, str]] = None

    def register(self, visitor) -> list:
        ...


class Composite(Component):
    is_composite: bool
    children: Optional[List[Union[Component, "Composite"]]]


class Visitor(Protocol):
    ...


def register(component: Union[Component, Composite], visitor: Visitor) -> None:
    if component.is_composite and component.children:
        for child in component.children:
            register(child, visitor)
    component.register(visitor)


class Renderer:
    @classmethod
    def accept(cls, obj: Component) -> None:
        obj.rendition = cls.format_component(obj)

    @classmethod
    def render(cls, component) -> str:
        if component.is_composite:
            return "".join(list(map(lambda x: x.rendition, component.children)))
        return component.children

    @classmethod
    def format_component(cls, obj: Component) -> str:
        if obj.children:
            return f"<{obj.name}>{cls.render(obj)}</{obj.name}>"
        return f"<{obj.name}/>"


class Importer:
    temp_storage = {"react": {"React"}, "imported": set()}

    @classmethod
    def accept(cls, obj: Component) -> dict:
        if obj.name not in cls.temp_storage["imported"]:
            cls.temp_storage["imported"].add(obj.name)
            cls.format_imports(cls.replace_import(obj))
            obj.imports = cls.temp_storage
            return cls.temp_storage

    @classmethod
    def replace_import(cls, obj: Component) -> dict:
        return {
            obj.name: settings.IMPORTS.get(obj.package)
            if obj.name not in settings.REPLACE_COMPONENTS
            else settings.REPLACE_COMPONENTS.get(obj.name)["package"]
        }

    @classmethod
    def format_imports(cls, imports: dict) -> None:
        for k, v in imports.items():
            if v not in cls.temp_storage:
                cls.temp_storage[v] = set()
            cls.temp_storage[v].add(k)

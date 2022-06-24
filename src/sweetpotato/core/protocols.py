from typing import Protocol, Optional, List, Iterable, Union
from sweetpotato.config import settings


class Component(Protocol):
    name: str
    parent: "Component"
    is_composite: bool = False
    package: dict
    children: Optional[Union[int, str]] = None

    def register(self, visitor) -> list:
        ...


class Composite(Component):
    is_composite: bool = True
    children: Optional[List[Union["Component", "Composite"]]] = None


class Visitor(Protocol):
    ...


def register(children: Iterable[Component], visitor: Visitor) -> Union[dict, list]:
    res = []
    for child in children:
        value = child.register(visitor)
        if value not in res:
            res.append(value)
    return res


class Renderer:
    @classmethod
    def accept(cls, obj: Component) -> str:
        left, right = cls.format_name(obj)
        if obj.is_composite:
            children = "".join([cls.accept(child) for child in obj.children])
            return f"{left}{children}{right}"
        return f"{left}<{obj.name}>{obj.children}</{obj.name}>{right}"

    @classmethod
    def format_name(cls, obj: Component) -> tuple:
        return (
            (f"<{obj.parent.name}>", f"</{obj.parent.name}>")
            if obj.parent
            else ("", "")
        )


class Importer:
    temp_storage = {}

    @classmethod
    def accept(cls, obj: Component) -> dict:
        for child in obj.children:
            cls.format_imports(cls.replace_import(child))
        cls.format_imports(cls.replace_import(obj))
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

from typing import List

from sweetpotato.core.base import Component, Composite


class NavigationComponent(Component):
    pass


class NavigationContainer(Composite):
    pass


class Screen(Composite):
    """React navigation screen component.
    Args:
        functions: String representation of .js based functions.
        state: Dictionary of allowed state values for component.
    Attributes:
        screen_name (str): Name of specific screen.
        import_name (str): Name of .js const for screen.
        state (dict): Dictionary of allowed state values for component.
        functions (str): String representation of .js based functions.
    """

    is_screen = True

    def __init__(self, screen_name: str, screen_type, **kwargs) -> None:
        kwargs.update(
            {
                "name": f"'{screen_name}'",
                "component": "".join([word.title() for word in screen_name.split(" ")]),
            }
        )
        self.name = f"{screen_type}.Screen"
        self.import_name = kwargs["component"]
        self.package = f"./{kwargs['component']}.js"
        super().__init__(**kwargs)
        self.set_parent(self.children)

    def set_parent(self, children):
        self.children[0].is_root = True
        for child in children:
            if child.is_composite:
                self.set_parent(child.children)
            child.parent = self.import_name


class BaseNavigator(Composite):
    def __init__(self, name: str = None, **kwargs) -> None:
        if name:
            component_name = self.name.split(".")
            component_name[0] = name
            self.name = ".".join(component_name)

        kwargs.update(**dict(variables=[f"const {self.name} = {self.import_name}()"]))
        super().__init__(**kwargs)
        self.variables = [f"const {self.name} = {self.import_name}()"]

        self.screen_type = self.name.split(".")[0]
        self.name = f"{self.name}.Navigator"

    def screen(self, screen_name: str, children: List) -> None:
        self.children.append(
            Screen(
                screen_name=screen_name, screen_type=self.screen_type, children=children
            )
        )


class StackNavigator(BaseNavigator):
    """Abstraction of React Navigation StackNavigator component.

    See https://reactnavigation.org/docs/stack-navigator
    """

    pass


class TabNavigator(BaseNavigator):
    """Abstraction of React Navigation TabNavigator component.

    See https://reactnavigation.org/docs/bottom-tab-navigator
    """

    pass


class Tab(BaseNavigator):
    """Abstraction of React Navigation TabNavigator component.

    See https://reactnavigation.org/docs/bottom-tab-navigator
    """

    pass


def create_bottom_tab_navigator(name: str = None) -> Tab:
    return Tab(name=name)

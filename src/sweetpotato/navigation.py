"""Contains classes based on React Navigation components.


See `React Navigation <https://reactnavigation.org/docs/getting-started/#>`_
"""

from typing import Optional, Union

from sweetpotato.core.base import Composite, Component
from sweetpotato.core.protocols import ComponentType, CompositeType, CompositeVar


class NavigationContainer(Composite):
    """React Navigation NavigationContainer component."""


class RootNavigation(Component):
    """React Navigation component based on for navigating without the prop.

    Based on https://reactnavigation.org/docs/navigating-without-navigation-prop/
    so that we don't have to pass the prop between screens.
    """

    functions = [
        "export function navigate(name,params){if(navigationRef.isReady()){navigationRef.navigate(name,params);}}"
    ]


class Screen(Composite):
    """React Navigation Screen component.

    Args:
        functions: List of string representation of .js based functions.
        state: Dictionary of allowed state values for component.
        kwargs: Arbitrary keyword arguments.

    Attributes:
        screen_name: Name of specific screen.
        import_name: Name of .js const for screen.
        functions: String representation of .js based functions.
    """

    is_root: bool = True
    parent = None

    def __init__(
        self,
        screen_type: str,
        screen_name: str,
        functions: Optional[list[str]] = None,
        **kwargs,
    ) -> None:
        kwargs.update(
            {
                "name": f"'{screen_name}'",
            }
        )
        super().__init__(**kwargs)
        self._functions = functions if functions else []
        self.screen_type = f"{screen_type}.{self.name}"
        self.screen_name = screen_name
        self.import_name = "".join(
            [word.title() for word in self.screen_name.split(" ")]
        )
        self.package = f"./src/{self.import_name}.js"
        self.__set_parent(self._children)

    def __set_parent(self, children: list[Union[CompositeType, ComponentType]]) -> None:
        """Sets top level component as root and sets each parent to self.

        Args:
            children: List of components.
        """
        self._children[0].is_root = True
        for child in children:
            if child.is_composite:
                self.__set_parent(child._children)
            child.parent = self.import_name

    def __repr__(self):
        children = (
            f"{'{'}'{self.screen_name}'{'}'}>{'{'}() => <{self.import_name}/> {'}'}"
        )
        return f"<{self.screen_type} name={children}</{self.screen_type}>"


class BaseNavigator(Composite):
    """Abstraction of React Navigation Base Navigation component.

    Args:
        name: Name/type of navigator.
        kwargs: Arbitrary keyword arguments.

    Attributes:
        name: Name/type of navigator.
        variables: Contains variables (if any) belonging to given component.

    Todo:
        * Add specific props from React Navigation.
    """

    def __init__(self, name: str = None, **kwargs) -> None:
        super().__init__(**kwargs)
        self.name = self._set_custom_name(name=name) if name else self.name
        self.variables = f"const {self.name} = {self.import_name}()"
        self.screen_type = self.name.split(".")[0]
        self.name = f"{self.name}.Navigator"

    @staticmethod
    def _set_custom_name(name: str) -> str:
        component_name = name.split(".")
        component_name[0] = name
        return (".".join(component_name)).title()

    def screen(
        self,
        screen_name: str,
        children: CompositeVar,
        functions: Optional[list] = None,
        state: Optional[dict[str, str]] = None,
    ) -> None:
        """Instantiates and adds screen to navigation component and increments screen count.

        Args:
            screen_name: Name of screen component.
            children: List of child components.
            functions: String representation of .js functions for component.
            state: Dictionary of applicable state values for component.
        """
        screen_type = self.name.split(".")[0]
        self._children.append(
            Screen(
                screen_name=screen_name,
                screen_type=screen_type,
                children=children,
                functions=functions,
                state=state,
            )
        )


class StackNavigator(BaseNavigator):
    """Abstraction of React Navigation StackNavigator component.

    See https://reactnavigation.org/docs/stack-navigator
    """


class TabNavigator(BaseNavigator):
    """Abstraction of React Navigation TabNavigator component.

    See https://reactnavigation.org/docs/bottom-tab-navigator
    """


def create_bottom_tab_navigator(name: Optional[str] = None) -> TabNavigator:
    """Function representing the createBottomTabNavigator function in react-navigation.

    Args:
        name: name of navigator.

    Returns:
        Tab navigator.
    """
    return TabNavigator(name=name)


def create_native_stack_navigator(name: Optional[str] = None) -> StackNavigator:
    """Function representing the createNativeStackNavigator function in react-navigation.

    Args:
        name: name of navigator.

    Returns:
        Stack navigator.
    """
    return StackNavigator(name=name)

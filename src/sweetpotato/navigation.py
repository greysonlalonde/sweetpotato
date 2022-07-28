"""Contains classes based on React Navigation components.


See `React Navigation <https://reactnavigation.org/docs/getting-started/#>`_
"""

from typing import Optional

from sweetpotato.config import settings
from sweetpotato.core.base import Composite, RootComponent
from sweetpotato.core.protocols import CompositeVar


class NavigationContainer(Composite):
    """React Navigation NavigationContainer component."""


class RootNavigation(RootComponent):
    """React Navigation component based on navigating without the prop.

    Based on https://reactnavigation.org/docs/navigating-without-navigation-prop/
    so that we don't have to pass the prop between screens.
    """

    is_composite = False
    functions = [
        "export function navigate(name,params){if(navigationRef.isReady()){navigationRef.navigate(name,params);}}"
    ]


class Screen(RootComponent):
    """React Navigation Screen component.

    Args:
        screen_type: Navigator name/type prefix, shown as {screen_name}.Screen.
        screen_name: Name of screen.
        kwargs: Arbitrary keyword arguments.

    Attributes:
        screen_type: Navigator name/type prefix, shown as {screen_name}.Screen.
    """

    package_root: str = f"./{settings.SOURCE_FOLDER}"

    def __init__(
        self,
        screen_type: str,
        screen_name: str,
        **kwargs,
    ) -> None:
        super().__init__(component_name=screen_name, **kwargs)
        self.screen_type = f"{screen_type}.{self.name}"

    def __repr__(self) -> str:
        children = (
            f"{'{'}'{self.component_name}'{'}'}>{'{'}() => <{self.import_name}/> {'}'}"
        )
        return f"<{self.screen_type} name={children}</{self.screen_type}>"


class BaseNavigator(Composite):
    """Abstraction of React Navigation Base Navigation component.

    Args:
        name: Name/type of navigator.
        kwargs: Arbitrary keyword arguments.

    Attributes:
        name: Name/type of navigator.

    Todo:
        * Add specific props from React Navigation.
    """

    def __init__(self, name: str = None, **kwargs) -> None:
        super().__init__(**kwargs)
        self.name = self._set_custom_name(name=name) if name else self.name
        self._variables = [f"const {self.name} = {self.import_name}()"]
        self.name = f"{self.name}.Navigator"
        self._children.append(RootNavigation())

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

"""Contains classes based on React Navigation components.

See `React Navigation <https://reactnavigation.org/docs/getting-started/#>`_
"""

from typing import Optional

from sweetpotato.core.base import Composite


class NavigationContainer(Composite):
    """React Navigation NavigationContainer component."""

    pass


class Screen(Composite):
    """React Navigation Screen component.

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

    def __init__(
        self,
        screen_name: str,
        screen_type: str,
        functions=None,
        state=None,
        **kwargs,
    ) -> None:
        if state is None:
            state = {}
        if functions is None:
            functions = []
        kwargs.update(
            {
                "name": f"'{screen_name}'",
            }
        )
        super().__init__(**kwargs)
        self.name = f"{screen_type}.Screen"
        self.import_name = "".join([word.title() for word in screen_name.split(" ")])
        self.package = f"./src/{self.import_name}.js"
        self.functions = functions
        self.state = state
        self.set_parent(self.children)

    def set_parent(self, children: list):
        """Sets top level component as root and sets each parent to self.

        Args:
            children (list): List of components.

        Returns:
            None
        """
        self.children[0].is_root = True
        for child in children:
            if child.is_composite:
                self.set_parent(child.children)
            child.parent = self.import_name

    def __repr__(self):
        return f"<{self.name}{self.attrs}>{'{'}() => <{self.import_name}/> {'}'}</{self.name}>"


class BaseNavigator(Composite):
    """Abstraction of React Navigation Base Navigation component.

    Args:
        kwargs: Any of ...

    Attributes:
        name (str): Name/type of navigator.
        _screens (dict): Dictionary of name: :class:`~sweetpotato.navigation.Screen`.
        _screen_number (int): Counter to determine screen number.
        _variables (set): Set of .js components specific to navigator type.

    Todo:
        * Add specific props from React Navigation.
    """

    def __init__(self, name: str = None, **kwargs) -> None:
        super().__init__(**kwargs)
        if name:
            component_name = self.name.split(".")
            component_name[0] = name
            self.name = (".".join(component_name)).title()
        self.variables = [f"const {self.name} = {self.import_name}()"]
        self.screen_type = self.name.split(".")[0]
        self.name = f"{self.name}.Navigator"

    def screen(
        self,
        screen_name: str,
        children: list,
        functions: Optional[list[str]] = None,
        state: Optional[dict] = None,
    ) -> None:
        """Instantiates and adds screen to navigation component and increments screen count.

        Args:
            screen_name: Name of screen component.
            children: List of child components.
            functions: String representation of .js functions for component.
            state: Dictionary of applicable state values for component.

        Returns:
            None
        """
        self.children.append(
            Screen(
                screen_name=screen_name,
                screen_type=self.screen_type,
                children=children,
                functions=functions,
                state=state,
            )
        )


class Stack(BaseNavigator):
    """Abstraction of React Navigation StackNavigator component.

    See https://reactnavigation.org/docs/stack-navigator
    """

    pass


class Tab(BaseNavigator):
    """Abstraction of React Navigation TabNavigator component.

    See https://reactnavigation.org/docs/bottom-tab-navigator
    """

    pass


def create_bottom_tab_navigator(name: Optional[str] = None) -> Tab:
    """Function representing the createBottomTabNavigator function in react-navigation.

    Args:
        name (str, optional): name of navigator.

    Returns:
        Tab navigator.
    """
    return Tab(name=name)


def create_native_stack_navigator(name: Optional[str] = None) -> Stack:
    """Function representing the createNativeStackNavigator function in react-navigation.

    Args:
        name (str, optional): name of navigator.

    Returns:
        Tab navigator.
    """
    return Stack(name=name)

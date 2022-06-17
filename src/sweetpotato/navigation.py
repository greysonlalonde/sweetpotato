"""Contains classes based on React Navigation components.

See https://reactnavigation.org
"""
import json
import re
from typing import Optional

from sweetpotato.components import Component
from sweetpotato.components import SafeAreaProvider
from sweetpotato.config import settings
from sweetpotato.core.exceptions import NoChildrenError
from sweetpotato.ui_kitten import ApplicationProvider


class Screen(Component):
    """React navigation screen component.

    Args:
        functions: String representation of .js based functions.
        state: Dictionary of allowed state values for component.

    Attributes:
        _type (str): Screen type.
        _screen_name (str): Name of specific screen.
        _const_name (str): Name of .js const for screen.
        _state (dict): Dictionary of allowed state values for component.
        _functions (str): String representation of .js based functions.

    Todo:
        * Evaluate changing from Component inheritance to a BaseScreen class
          and use as an interface to the underlying components.
    """

    def __init__(
        self, functions: Optional[str], state: Optional[dict] = None, **kwargs
    ) -> None:
        super().__init__(**kwargs)
        if state is None:
            state = {}
        if functions is None:
            functions = ""
        self._type = kwargs.get("type")
        self._screen_name = kwargs.get("screen_name")
        self._const_name = "".join(
            [word.title() for word in self._screen_name.split(" ")]
        )
        self._state = state
        self._functions = functions

    def write_import(self) -> str:
        """Returns name of .js const for screen as the file import.

        Returns:
            Screen name.
        """
        return self._const_name

    def write_state(self) -> str:
        """Writes component state in JSON format.

        Returns:
            React Native friendly string representation of state.
        """
        state = "".join([f"{k}: {json.dumps(v)},\n" for k, v in self._state.items()])
        return f'this.state={"{"}{state}{"}"}'

    def write_component(self) -> str:
        """Render React Native friendly string representation of component.

        Note:
            Need to look at removing this and keeping parent method or splitting to
            a different inheritance.

        Returns:
            React Native friendly string representation.

        Todo:
            * Need to refactor this into smaller helper methods.
        """
        screen_name = "{'" + self._screen_name + "'}"
        screen_name_spaced = "{" + self._const_name + "}"
        imports = [child.write_import() for child in self._children]
        child_components = "".join(
            [child.write_component() for child in self._children]
        )
        constructor = "{constructor(props){super(props);<STATE>}"
        constructor = constructor.replace("<STATE>", self.write_state())
        const = f"{constructor}{self._functions}\nrender() {'{'}return(\n{child_components}\n)\n{'}}'}"
        packages = ""
        for package in imports:
            packages += "\n".join(
                [f'import {v} from "{k}";'.replace("'", "") for k, v in package.items()]
            )

        with open(
            f"{settings.REACT_NATIVE_PATH}/src/{self._const_name}.js", "w"
        ) as file:
            file.write(
                f"import React from 'react';\n{packages}\nexport class {self._const_name} extends "
                f"React.Component {const};\n "
            )
        return f"<{self._type}.{self._name} name={screen_name} component={screen_name_spaced}/>"


class BaseNavigator(Component):
    """Abstraction of React Navigation Base Navigation component.

    Args:
        kwargs: Any of ...

    Attributes:
        _name (str): Name/type of navigator.
        _screens (dict): Dictionary of name: :class:`~sweetpotato.navigation.Screen`.
        _screen_number (int): Counter to determine screen number.
        _variables (set): Set of .js components specific to navigator type.

    Todo:
        * Add specific props from React Navigation.
    """

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self._name = ".".join(re.findall("[A-Z][^A-Z]*", self.__class__.__name__))
        self._screens = dict()
        self._screen_number = 0
        self._variables.add(f"const {self._type} = {self._react_component}();")

    def write_component(self) -> str:
        """Render React Native string representation of component.

        Note:
            Need to look at removing this and keeping parent method or splitting to
            a different inheritance.

        Returns:
            String representation of component.
        """
        comp_str = ""
        if not isinstance(self._screens, type(None)):
            comp_str += "\n".join(
                [component.write_component() for component in self._screens.values()]
            )
            return f"\n<{self._name} {self._attrs}>\n{comp_str}\n</{self._name}>"
        return f"\n<{self._type} {self._attrs}></{self._type}>"

    def write_import(self) -> dict:
        """Write imports.

        Returns:
            Imports for children and self.
        """
        imports = {
            f"./{settings.SOURCE_FOLDER}/{child.write_import()}.js": child.write_import()
            for child in self._screens.values()
        }
        imports[self._package] = self._react_component
        return imports

    def screen(
        self,
        screen_name: str,
        children: list,
        functions: Optional[str] = None,
        state: Optional[dict] = None,
    ):
        """Instantiates and adds screen to navigation component and increments screen count.

        Args:
            screen_name: Name of screen component.
            children: List of child components.
            functions: String representation of .js functions for component.
            state: Dictionary of applicable state values for component.

        Returns:
            None
        """
        screen = Screen(
            type=self._type,
            state=state,
            screen_name=screen_name,
            functions=functions,
            children=children,
        )
        self._screen_number += 1
        self._screens[self._screen_number] = screen


class NavigationContainer(Component):
    """
    React-navigation NavigationContainer component.

    Keyword Args:
        theme: Optional theme for UI Kitten if turned on.
        kwargs: Any of ...

    Attributes:
        _theme (str): Optional theme for UI Kitten if turned on.
        _attrs (str): String representation of key=value pair for RootNavigation.

    Todo:
        * Refactor _attrs method here.
    """

    def __init__(self, theme: Optional[dict] = None, **kwargs) -> None:
        self._theme = theme
        super().__init__(**kwargs)
        self._attrs += "ref={this.state.navigation}"

    def write_component(self) -> str:
        """Render react-native friendly string representation of component.

        Note:
            Need to look at removing this and keeping parent method or splitting to
            a different inheritance.

        Returns:
            React Native friendly string representation of state.

        Raises:
            :exc:`sweetpotato.core.exceptions.NoChildrenError`
        """

        if self._children:
            app = SafeAreaProvider(children=self._children)
            if settings.USE_UI_KITTEN:
                app = ApplicationProvider(children=[app], theme=self._theme)
            return (
                f"<{self._name} {self._attrs}>{app.write_component()}\n</{self._name}>"
            )

        raise NoChildrenError("Navigator component needs children")


class DrawerNavigator(BaseNavigator):
    """Abstraction of React Navigation Drawer component.

    See https://reactnavigation.org/docs/drawer-navigator
    """

    pass


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

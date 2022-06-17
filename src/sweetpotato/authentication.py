"""Contains plugins for authentication.

Attributes:
    LOGIN_DICT: ...
    LOGIN_CHILDREN: ...

"""
import json
from typing import Optional

from sweetpotato.components import Button
from sweetpotato.components import Component
from sweetpotato.components import TextInput
from sweetpotato.components import View
from sweetpotato.config import settings
from sweetpotato.core.exceptions import NoChildrenError
from sweetpotato.navigation import StackNavigator
from sweetpotato.ui_kitten import Layout

view_style = {
    "justifyContent": "center",
    "alignItems": "center",
    "width": "100%",
    "flex": 1,
}
row_style = {
    "flexDirection": "row",
    "marginTop": 4,
    "width": "100%",
    "justifyContent": "center",
}

username_row = View(
    style=row_style,
    children=[
        TextInput(
            placeholder="Username",
            value="this.state.username",
            onChangeText="(text) => this.setUsername(text)",
        )
    ],
)
password_row = View(
    style=row_style,
    children=[
        TextInput(
            placeholder="Password",
            value="this.state.password",
            onChangeText="(text) => this.setPassword(text)",
            secureTextEntry="this.state.secureTextEntry",
        )
    ],
)
LOGIN_SCREEN = dict(
    style=view_style,
    children=[
        username_row,
        password_row,
        Button(title="SUBMIT", onPress="() => this.login()"),
    ],
)

auth_state = {"username": "", "password": "", "secureTextEntry": True}


class Login(Component):
    """Plugin component for handling authentication.

    Args:
        children: ...
        functions: ...

    Attributes:
        _functions: ...
        _screen_name: ...
        _const_name: ...
        _attrs: ...
        _children: ...
        _state: ...
        _stack: ...

    Todo:
        * Refactor into a child of :class:`sweetpotato.navigation.Screen`.

    """

    def __init__(
        self, children: Optional[list] = None, functions: Optional[str] = None, **kwargs
    ) -> None:
        super().__init__(**kwargs)
        if not children:
            children = (
                [Layout(**LOGIN_SCREEN)]
                if settings.USE_UI_KITTEN
                else [View(**LOGIN_SCREEN)]
            )
        if functions is None:
            functions = (
                settings.SET_CREDENTIALS
                + settings.LOGIN_FUNCTION
                + settings.STORE_SESSION
                + settings.STORE_DATA
            )
        self._functions = functions
        self._screen_name = "Login"
        self._const_name = "Login"
        self._attrs = "login={this.login}"
        self._children = children
        self._state = kwargs.get("state", auth_state)
        self._stack = StackNavigator()

    def write_import(self) -> dict:
        imports = {
            f"./{settings.REACT_NATIVE_PATH}/{settings.SOURCE_FOLDER}/{child.write_import()}.js": child.write_import()
            for child in self._stack._screens.values()
        }
        imports[self._package] = self._react_component
        self_imports = self._stack.write_import()
        self_imports.update(
            **{
                "@react-native-async-storage/async-storage": "AsyncStorage",
                "expo-secure-store": "* as SecureStore",
            }
        )
        return self_imports

    def write_component(self) -> str:
        self._stack.write_import()
        imports = [child.write_import() for child in self._children]
        imports.append(self.write_import())
        packages = ""
        for package in imports:
            packages += "\n".join(
                [f'import {v} from "{k}";'.replace("'", "") for k, v in package.items()]
            )
        self._stack.screen(
            screen_name="Login",
            functions=self._functions,
            state=self._state,
            children=self._children,
        )
        return self._stack.write_component()

    def write_state(self) -> str:
        """Writes component state in JSON format.

        Return:
            React Native friendly string representation of state.
        """
        return "".join([f"{k}: {json.dumps(v)},\n" for k, v in self._state.items()])


class AuthenticationProvider(Component):
    """Authentication provider for app.

    Attributes:
        _screens (set): Set of all screens under authentication.
        _screen_number (int): Amount of screens.
    """

    def __init__(self, **kwargs):
        self._screens = dict()
        self._screen_number = 0
        super().__init__(**kwargs)

    def write_component(self) -> str:
        """Render react-native friendly string representation of component.

        Return:
            React Native friendly string representation of state

        Raises:
            :class:`sweetpotato.core.exceptions.NoChildrenError`
        """
        if self._children:
            children = "".join([child.write_component() for child in self._children])
            self._screen_number += 1
            self._screens[self._screen_number] = Login()
            auth = f"{'{'}this.state.isAuthenticated ? {children} : {self._screens[self._screen_number]}{'}'}"
            return auth
        raise NoChildrenError(name=self._name)

    def write_import(self) -> dict:
        """Write imports.

        Return:
            Imports for children and self
        """
        imports = {
            f"./{settings.REACT_NATIVE_PATH}/{settings.SOURCE_FOLDER}/{child.write_import()}.js": child.write_import()
            for child in self._screens.values()
        }
        imports[self._package] = self._react_component
        return imports

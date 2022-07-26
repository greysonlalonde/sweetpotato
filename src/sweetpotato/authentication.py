"""Contains plugins for authentication.

Todo:
    * Need to refactor the entire module to reflect current functionality.
"""
from typing import Optional, Callable

from sweetpotato.components import (
    Button,
    TextInput,
    View,
)
from sweetpotato.components import Composite
from sweetpotato.config import settings
from sweetpotato.navigation import create_native_stack_navigator


def login() -> dict:
    """Provides default login plugin screen.

    Returns:
        Dictionary of styles and components to be passed to a View or Layout instance.
    """
    view_style: dict = {
        "justifyContent": "center",
        "alignItems": "center",
        "width": "100%",
        "flex": 1,
    }
    row_style: dict = {
        "flexDirection": "row",
        "marginTop": 4,
        "width": "100%",
        "justifyContent": "center",
    }
    username_row = View(
        style=row_style,
        children=[
            TextInput(
                placeholder="'Username'",
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
    login_screen = dict(
        style=view_style,
        children=[
            username_row,
            password_row,
            Button(title="SUBMIT", onPress="() => this.login()"),
        ],
    )
    return login_screen


class AuthenticationProvider(Composite):
    """Authentication provider for app.

    Args:
        functions: list of functions passes to authentication component.
        login_screen: function returning login screen component.
        login_screen_name: Name of login screen.
        kwargs: Arbitrary keyword arguments.

    Attributes:
        _screens: Set of all screens under authentication.
        _screen_number: Amount of screens.
    """

    package = None

    def __init__(
        self,
        functions: list[str] = None,
        login_screen: Optional[Callable[[], dict]] = None,
        login_screen_name: Optional[str] = None,
        **kwargs,
    ) -> None:
        if functions is None:
            functions = [
                settings.SET_CREDENTIALS,
                settings.LOGIN_FUNCTION,
                settings.STORE_SESSION,
                settings.STORE_DATA,
            ]
        super().__init__(**kwargs)
        login_screen = login if not login_screen else login_screen
        login_screen_name = "Login" if not login_screen_name else login_screen_name

        stack = create_native_stack_navigator()
        stack.screen(
            state={"username": "", "password": "", "secureTextEntry": True},
            children=[View(functions=functions, **login_screen())],
            screen_name=login_screen_name,
        )

        self._children.append(stack)

    def __repr__(self) -> str:
        authenticated = "".join(map(repr, [self._children[0]]))
        return f"{'{'}this.state.authenticated ? {authenticated} : {self._children[1]}{'}'}"

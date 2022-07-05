"""Contains plugins for authentication.

Todo:
    * Need to refactor the entire module to reflect current functionality.
"""
from sweetpotato.components import (
    Button,
    TextInput,
    View,
)
from sweetpotato.components import Composite
from sweetpotato.config import settings
from sweetpotato.navigation import create_native_stack_navigator

#
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


def login():
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
    LOGIN_SCREEN = dict(
        style=view_style,
        children=[
            username_row,
            password_row,
            Button(title="SUBMIT", onPress="() => this.login()"),
        ],
    )
    return LOGIN_SCREEN


#
# auth_state = {"username": "", "password": "", "secureTextEntry": True}


class AuthenticationProvider(Composite):
    """Authentication provider for app.

    Attributes:
        _screens (set): Set of all screens under authentication.
        _screen_number (int): Amount of screens.
    """

    def __init__(self, functions: list = None, login_screen=None, **kwargs):
        if login_screen is None:
            login_screen = login
        if functions is None:
            functions = [
                settings.SET_CREDENTIALS,
                settings.LOGIN_FUNCTION,
                settings.STORE_SESSION,
                settings.STORE_DATA,
            ]

        stack = create_native_stack_navigator()
        stack.screen(
            state={"username": "", "password": "", "secureTextEntry": True},
            functions=functions,
            children=[View(**login_screen())],
            screen_name="Login",
        )
        # stack.screen(children=kwargs.pop('children'), screen_name="Authenticated")
        super().__init__(**kwargs)
        self.children.append(stack)

    def __repr__(self):
        return f"{'{'}this.state.authenticated ? {''.join(map(repr, [self.children[0]]))} : {self.children[1]}{'}'}"

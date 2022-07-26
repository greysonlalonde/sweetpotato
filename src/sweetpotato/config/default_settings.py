"""Default sweetpotato settings.

For the full list of settings and their values, see
https://sweetpotato.readthedocs.io/en/latest/settings.html
"""
from pathlib import Path

import sweetpotato.functions.authentication_functions as auth_functions
from sweetpotato import defaults
from sweetpotato.core import ThreadSafe


class ReactNavigation:
    """Provides changeable configuration for React Navigation packages."""

    # Navigation configuration
    native: str = (
        "@react-navigation/native"  #: Default package name of @react-navigation/native
    )
    bottom_tabs: str = "@react-navigation/bottom-tabs"  #: Default package name of @react-navigation/bottom-tabs
    stack: str = "@react-navigation/native-stack"  #: Default package name of @react-navigation/native-stack


class UIKitten:
    """Provides changeable configuration for UI Kitten packages."""

    # UI Kitten configuration
    ui_kitten_components: str = (
        "@ui-kitten/components"  #: Default package name of @ui-kitten
    )


class Settings(metaclass=ThreadSafe):
    """Provides and allows user to override default configuration."""

    # App configuration
    APP_COMPONENT: str = (
        defaults.APP_COMPONENT
    )  #: Name of application component, defaults to `'App'`.
    APP_REPR: str = (
        defaults.APP_REPR_DEFAULT
    )  #: String representation of .js application class component.

    # UI Kitten settings
    USE_UI_KITTEN: bool = False  #: Indicates whether to use @ui-kitten/components.
    UI_KITTEN_REPLACEMENTS: dict = (
        {}
    )  #: Replaces equivalent react native components with @ui-kitten components.

    # Functions
    FUNCTIONS: dict = {}  #: Default generic functions.
    USER_DEFINED_FUNCTIONS: dict = {}  #: Provided UDFs, if any.

    # User defined components
    USER_DEFINED_COMPONENTS: dict = {}  #: Provided user defined components, if any.

    # API settings
    API_URL: str = "http://127.0.0.1:8000"  #: URL for API calls.

    # Authentication settings
    USE_AUTHENTICATION: bool = (
        False  #: Indicates whether to use authentication methods.
    )
    LOGIN_COMPONENT: str = "Login"  #: Name of login component, defaults to `'Login'`.
    LOGIN_FUNCTION: str = auth_functions.LOGIN.replace(
        "API_URL", API_URL
    )  #: Login function for authentication.
    LOGOUT_FUNCTION: str = auth_functions.LOGOUT.replace(
        "API_URL", API_URL
    )  #: Logout function for authentication.
    SET_CREDENTIALS: str = (
        auth_functions.SET_CREDENTIALS
    )  #: Credential setting function for authentication.
    STORE_DATA: str = (
        auth_functions.STORE_DATA
    )  #: Data storage setting function for authentication.
    RETRIEVE_DATA: str = (
        auth_functions.RETRIEVE_DATA
    )  #: Data retrieval function for authentication.
    STORE_SESSION: str = (
        auth_functions.STORE_SESSION
    )  #: Session storage function for authentication.
    RETRIEVE_SESSION: str = (
        auth_functions.RETRIEVE_SESSION
    )  #: Session retrieval function for authentication.
    REMOVE_SESSION: str = (
        auth_functions.REMOVE_SESSION
    )  #: Session removal function for authentication.
    TIMEOUT: str = (
        auth_functions.TIMEOUT
    )  #: Generic timeout function for authentication.
    AUTH_FUNCTIONS: dict = {
        APP_COMPONENT: LOGIN_FUNCTION,
        LOGIN_COMPONENT: SET_CREDENTIALS,
    }  #: Dictionary of authentication functions and corresponding components.

    # Navigation settings
    USE_NAVIGATION: bool = False  #: Indicates whether to use @react-navigation/native.

    # React Native settings
    RESOURCE_FOLDER: str = "frontend"  #: Name of expo project resource folder.
    SOURCE_FOLDER: str = "src"  #: Name of expo project component folder.
    REACT_NATIVE_PATH: str = f"{Path(__file__).resolve().parent.parent}/{RESOURCE_FOLDER}"  #: Absolute path to expo project.

    # Imports and replacements
    IMPORTS: dict = {
        "components": "react-native",
        "ui_kitten": UIKitten.ui_kitten_components,
        "navigation": ReactNavigation.native,
        "authentication": "Authentication",
    }  #: Major packages and corresponding sweetpotato modules.
    REPLACE_COMPONENTS: dict = {
        "StackNavigator": {
            "package": ReactNavigation.stack,
            "import": "createNativeStackNavigator",
            "name": "Stack",
        },
        "TabNavigator": {
            "package": ReactNavigation.bottom_tabs,
            "import": "createBottomTabNavigator",
            "name": "Tab",
        },
        "createNativeStackNavigator": {
            "package": ReactNavigation.stack,
        },
        "createBottomTabNavigator": {
            "package": ReactNavigation.bottom_tabs,
        },
        "SafeAreaProvider": {
            "package": "react-native-safe-area-context",
            "import": "SafeAreaProvider",
            "name": "SafeAreaProvider",
        },
        "NavigationContainer": {
            "package": ReactNavigation.native,
            "import": "NavigationContainer",
            "name": "NavigationContainer",
        },
        "AuthenticationProvider": {
            "name": "AuthenticationProvider",
            "import": "AuthenticationProvider",
        },
        "Authenticated": {
            "package": "./Authenticated",
            "name": "Authenticated",
            "import": "Authenticated",
        },
        "Login": {"package": "./Login", "name": "Login", "import": "Login"},
    }  #: Components with replaceable imports/names/packages, such as the Text component.

    APP_IMPORTS: set = set()  #: Set of all imports for application.

    @classmethod
    def __set_ui_kitten(cls) -> None:
        """Sets all necessary UI Kitten configuration for app."""
        cls.APP_IMPORTS.add("\nimport * as eva from '@eva-design/eva';")
        cls.APP_IMPORTS.add("\nimport {EvaIconsPack} from '@ui-kitten/eva-icons';")
        cls.REPLACE_COMPONENTS.update(
            **dict(
                TextInput={
                    "import": "Input",
                    "name": "Input",
                    "package": UIKitten.ui_kitten_components,
                },
                Input={
                    "package": UIKitten.ui_kitten_components,
                },
                Text={
                    "import": "Text",
                    "package": UIKitten.ui_kitten_components,
                },
                Button={
                    "import": "Button",
                    "package": UIKitten.ui_kitten_components,
                },
                ApplicationProvider={
                    "import": "ApplicationProvider",
                    "package": UIKitten.ui_kitten_components,
                },
            )
        )

    @classmethod
    def __set_authentication(cls) -> None:
        """Sets all necessary authentication configuration for app."""
        cls.APP_IMPORTS.add(
            "\nimport AsyncStorage from '@react-native-async-storage/async-storage';"
        )
        cls.APP_IMPORTS.add("\nimport * as SecureStore from 'expo-secure-store';")

    @classmethod
    def __set_navigation(cls) -> None:
        """Sets all necessary React Navigation configuration for app."""
        cls.APP_IMPORTS.add(
            "\nimport * as RootNavigation from './src/components/RootNavigation.js';"
        )

    @classmethod
    def __set_api(cls) -> None:
        """Sets API configuration for app."""
        cls.LOGIN_FUNCTION = auth_functions.LOGIN.replace("API_URL", cls.API_URL)
        cls.LOGOUT_FUNCTION = auth_functions.LOGOUT.replace("API_URL", cls.API_URL)
        cls.AUTH_FUNCTIONS = {
            cls.APP_COMPONENT: cls.LOGIN_FUNCTION,
            cls.LOGIN_COMPONENT: cls.SET_CREDENTIALS,
        }

    @classmethod
    def __set_react_native(cls) -> None:
        """Sets all necessary React Native configuration for app."""
        cls.REACT_NATIVE_PATH = (
            f"{Path(__file__).resolve().parent.parent}/{cls.RESOURCE_FOLDER}"
        )

    @classmethod
    def __setattr__(cls, key: str, value: str) -> None:
        if cls.__dict__.get(key, "") != value:
            setattr(cls, key, value)
        if cls.USE_UI_KITTEN:
            cls.__set_ui_kitten()
        if cls.USE_NAVIGATION:
            cls.__set_navigation()
        if cls.USE_AUTHENTICATION:
            cls.__set_authentication()
        if key in ["RESOURCE_FOLDER", "SOURCE_FOLDER"]:
            cls.__set_react_native()
        if key == "API_URL":
            cls.__set_api()

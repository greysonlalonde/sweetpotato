"""Default sweetpotato settings.

For the full list of settings and their values, see
https://sweetpotato.readthedocs.io/en/latest/settings.html
"""
from pathlib import Path

from sweetpotato import defaults
import sweetpotato.functions.authentication_functions as auth_functions
from sweetpotato.core import ThreadSafe


class ReactNavigation:
    """Provides changeable configuration for React Navigation packages."""

    # Navigation configuration
    native: str = "@react-navigation/native"
    bottom_tabs: str = "@react-navigation/bottom-tabs"
    stack: str = "@react-navigation/native-stack"


class UIKitten:
    """Provides changeable configuration for UI Kitten packages."""

    # UI Kitten configuration
    ui_kitten_components: str = "@ui-kitten/components"


class Settings(metaclass=ThreadSafe):
    """Provides and allows user to override default configuration."""

    # App configuration
    APP_COMPONENT: str = defaults.APP_COMPONENT
    APP_REPR: str = defaults.APP_REPR_DEFAULT

    # UI Kitten settings
    USE_UI_KITTEN: bool = False
    UI_KITTEN_REPLACEMENTS: dict = {}

    # Functions
    FUNCTIONS: dict = {}
    USER_DEFINED_FUNCTIONS: dict = {}

    # User defined components
    USER_DEFINED_COMPONENTS: dict = {}

    # API settings
    API_URL: str = "http://127.0.0.1:8000"

    # Authentication settings
    USE_AUTHENTICATION: bool = False
    LOGIN_COMPONENT: str = "Login"
    LOGIN_FUNCTION: str = auth_functions.LOGIN.replace("API_URL", API_URL)
    LOGOUT_FUNCTION: str = auth_functions.LOGOUT.replace("API_URL", API_URL)
    SET_CREDENTIALS: str = auth_functions.SET_CREDENTIALS
    STORE_DATA: str = auth_functions.STORE_DATA
    RETRIEVE_DATA: str = auth_functions.RETRIEVE_DATA
    STORE_SESSION: str = auth_functions.STORE_SESSION
    RETRIEVE_SESSION: str = auth_functions.RETRIEVE_SESSION
    REMOVE_SESSION: str = auth_functions.REMOVE_SESSION
    TIMEOUT: str = auth_functions.TIMEOUT
    AUTH_FUNCTIONS: dict = {
        APP_COMPONENT: LOGIN_FUNCTION,
        LOGIN_COMPONENT: SET_CREDENTIALS,
    }

    # Navigation settings
    USE_NAVIGATION: bool = False

    # React Native settings
    RESOURCE_FOLDER: str = "frontend"
    SOURCE_FOLDER: str = "src"
    REACT_NATIVE_PATH: str = (
        f"{Path(__file__).resolve().parent.parent}/{RESOURCE_FOLDER}"
    )

    # Imports and replacements
    IMPORTS: dict = {
        "components": "react-native",
        "ui_kitten": UIKitten.ui_kitten_components,
        "navigation": ReactNavigation.native,
        "authentication": "Authentication",
    }
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
            # "package": "",
            "name": "AuthenticationProvider",
            "import": "AuthenticationProvider",
        },
        "Authenticated": {
            "package": "./Authenticated",
            "name": "Authenticated",
            "import": "Authenticated",
        },
        "Login": {"package": "./Login", "name": "Login", "import": "Login"},
    }

    APP_IMPORTS: set = set()

    @classmethod
    def set_ui_kitten(cls) -> None:
        """Sets all necessary UI Kitten configuration for app.

        Returns:
            None
        """
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
    def set_authentication(cls) -> None:
        """Sets all necessary authentication configuration for app.

        Returns:
            None
        """
        cls.APP_IMPORTS.add(
            "\nimport AsyncStorage from '@react-native-async-storage/async-storage';"
        )
        cls.APP_IMPORTS.add("\nimport * as SecureStore from 'expo-secure-store';")

    @classmethod
    def set_navigation(cls) -> None:
        """Sets all necessary React Navigation configuration for app.

        Returns:
            None
        """
        cls.APP_IMPORTS.add(
            "\nimport * as RootNavigation from './src/components/RootNavigation.js';"
        )

    @classmethod
    def set_api(cls) -> None:
        """Sets API configuration for app.

        Returns:
            None
        """
        cls.LOGIN_FUNCTION = auth_functions.LOGIN.replace("API_URL", cls.API_URL)
        cls.LOGOUT_FUNCTION = auth_functions.LOGOUT.replace("API_URL", cls.API_URL)
        cls.AUTH_FUNCTIONS = {
            cls.APP_COMPONENT: cls.LOGIN_FUNCTION,
            cls.LOGIN_COMPONENT: cls.SET_CREDENTIALS,
        }

    @classmethod
    def set_react_native(cls) -> None:
        """Sets all necessary React Native configuration for app.

        Returns:
            None
        """
        cls.REACT_NATIVE_PATH = (
            f"{Path(__file__).resolve().parent.parent}/{cls.RESOURCE_FOLDER}"
        )

    @classmethod
    def __setattr__(cls, key: str, value: str) -> None:
        if cls.__dict__.get(key, "") != value:
            setattr(cls, key, value)
        if cls.USE_UI_KITTEN:
            cls.set_ui_kitten()
        if cls.USE_NAVIGATION:
            cls.set_navigation()
        if cls.USE_AUTHENTICATION:
            cls.set_authentication()
        if key in ["RESOURCE_FOLDER", "SOURCE_FOLDER"]:
            cls.set_react_native()
        if key == "API_URL":
            cls.set_api()

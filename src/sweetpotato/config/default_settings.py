"""Default sweetpotato settings.

For more information on this file, see
https://docs.sweetpotato.com/en/1.0/topics/settings/
For the full list of settings and their values, see
https://docs.sweetpotato.com/en/1.0/ref/settings/
"""
from pathlib import Path

import sweetpotato.defaults as defaults
import sweetpotato.functions.authentication_functions as auth_functions
from sweetpotato.core import ThreadSafe


# Navigation configuration
class ReactNavigation:
    """Provides changeable configuration for React Navigation packages."""

    native = "@react-navigation/native"
    bottom_tabs = "@react-navigation/bottom-tabs"
    stack = "@react-navigation/native-stack"


# UI Kitten configuration
class UIKitten:
    """Provides changeable configuration for UI Kitten packages."""

    ui_kitten_components = "@ui-kitten/components"


class Settings(metaclass=ThreadSafe):
    # App configuration
    APP_COMPONENT = defaults.APP_DEFAULT
    APP_PROPS = defaults.APP_PROPS_DEFAULT
    APP_REPR = defaults.APP_REPR_DEFAULT

    # UI Kitten settings
    USE_UI_KITTEN = False
    UI_KITTEN_REPLACEMENTS = {}

    # Functions
    FUNCTIONS = {}
    USER_DEFINED_FUNCTIONS = {}

    # User defined components
    USER_DEFINED_COMPONENTS = {}

    # API settings
    API_URL = "http://127.0.0.1:8000"

    # Authentication settings
    USE_AUTHENTICATION = False
    LOGIN_COMPONENT = "Login"
    LOGIN_FUNCTION = auth_functions.LOGIN.replace("API_URL", API_URL)
    LOGOUT_FUNCTION = auth_functions.LOGOUT.replace("API_URL", API_URL)
    SET_CREDENTIALS = auth_functions.SET_CREDENTIALS
    STORE_DATA = auth_functions.STORE_DATA
    RETRIEVE_DATA = auth_functions.RETRIEVE_DATA
    STORE_SESSION = auth_functions.STORE_SESSION
    RETRIEVE_SESSION = auth_functions.RETRIEVE_SESSION
    REMOVE_SESSION = auth_functions.REMOVE_SESSION
    TIMEOUT = auth_functions.TIMEOUT
    AUTH_FUNCTIONS = {APP_COMPONENT: LOGIN_FUNCTION, LOGIN_COMPONENT: SET_CREDENTIALS}

    # Navigation settings
    USE_NAVIGATION = False

    # React Native settings
    RESOURCE_FOLDER = "frontend"
    SOURCE_FOLDER = "src"
    REACT_NATIVE_PATH = f"{Path(__file__).resolve().parent.parent}/{RESOURCE_FOLDER}"

    # Imports and replacements
    IMPORTS = {
        "components": "react-native",
        "ui_kitten": UIKitten.ui_kitten_components,
        "navigation": ReactNavigation.native,
        "authentication": "Authentication",
    }
    REPLACE_COMPONENTS = {
        "Stack": {
            "package": ReactNavigation.stack,
            "import": "createNativeStackNavigator",
            "name": "StackNavigator",
        },
        "Tab": {
            "package": ReactNavigation.bottom_tabs,
            "import": "createBottomTabNavigator",
            "name": "TabNavigator",
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
            "package": "./AuthenticationProvider",
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

    REPLACE_ATTRS = {
        "theme": {
            "dark": "{...eva.dark}",
            "light": "{...eva.light}",
        },
        "onChangeText": "onChangeText",
        "onPress": "onPress",
        "value": "value",
        "secureTextEntry": "secureTextEntry",
    }

    APP_IMPORTS = set()

    @classmethod
    def set_ui_kitten(cls):
        cls.APP_IMPORTS.add("\nimport * as eva from '@eva-design/eva';")
        cls.APP_IMPORTS.add("\nimport {EvaIconsPack} from '@ui-kitten/eva-icons';")
        cls.REPLACE_COMPONENTS.update(
            **dict(
                TextInput={
                    "import": "Input",
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
    def set_authentication(cls):
        cls.APP_IMPORTS.add(
            "\nimport AsyncStorage from '@react-native-async-storage/async-storage';"
        )
        cls.APP_IMPORTS.add("\nimport * as SecureStore from 'expo-secure-store';")

    @classmethod
    def set_navigation(cls):
        cls.APP_IMPORTS.add(
            "\nimport * as RootNavigation from './src/components/RootNavigation.js';"
        )

    @classmethod
    def set_api(cls):
        cls.LOGIN_FUNCTION = auth_functions.LOGIN.replace("API_URL", cls.API_URL)
        cls.LOGOUT_FUNCTION = auth_functions.LOGOUT.replace("API_URL", cls.API_URL)
        cls.AUTH_FUNCTIONS = {
            cls.APP_COMPONENT: cls.LOGIN_FUNCTION,
            cls.LOGIN_COMPONENT: cls.SET_CREDENTIALS,
        }

    @classmethod
    def set_react_native(cls):
        cls.REACT_NATIVE_PATH = (
            f"{Path(__file__).resolve().parent.parent}/{cls.RESOURCE_FOLDER}"
        )

    @classmethod
    def __setattr__(cls, key, value):
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

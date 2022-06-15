"""
Default sweetpotato settings.
For more information on this file, see
https://docs.sweetpotato.com/en/1.0/topics/settings/
For the full list of settings and their values, see
https://docs.sweetpotato.com/en/1.0/ref/settings/
"""
from pathlib import Path

import sweetpotato.functions.authentication_functions as auth_functions
import sweetpotato.defaults as defaults

# App configuration
APP_COMPONENT = defaults.APP_DEFAULT
APP_PROPS = defaults.APP_PROPS_DEFAULT
APP_REPR = defaults.APP_REPR_DEFAULT


# Navigation configuration
class ReactNavigation:
    native = "@react-navigation/native"
    bottom_tabs = "@react-navigation/bottom-tabs"
    stack = "@react-navigation/native-stack"


# UI Kitten settings
class UIKitten:
    ui_kitten_components = "@ui-kitten/components"


USE_UI_KITTEN = False
UI_KITTEN_REPLACEMENTS = {}

if USE_UI_KITTEN:
    UI_KITTEN_REPLACEMENTS.update(
        {
            "TextInput": {"import": "Input", "package": UIKitten.ui_kitten_components},
            "Text": {
                "import": "Text",
                "package": UIKitten.ui_kitten_components,
            },
            "Button": {"import": "Button", "package": UIKitten.ui_kitten_components},
        }
    )

# Functions
FUNCTIONS = {}
USER_DEFINED_FUNCTIONS = {}

# User defined components
USER_DEFINED_COMPONENTS = {}

# Exports
DEFAULT_EXPORTS = {
    "@eva-design/eva": "* as eva",
    "./src/components/RootNavigation.js": "* as RootNavigation",
    "@react-native-async-storage/async-storage": "AsyncStorage",
    "expo-secure-store": "* as SecureStore",
}

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

# React Native settings
RESOURCE_FOLDER = "frontend"
SOURCE_FOLDER = "src"
REACT_NATIVE_PATH = f"{Path(__file__).resolve().parent.parent}/{RESOURCE_FOLDER}"

# Imports and replacements

IMPORTS = {
    "components": "react-native",
    "ui_kitten": UIKitten.ui_kitten_components,
    "navigation": ReactNavigation.native,
    "app": ReactNavigation.native,
}
REPLACE_COMPONENTS = {
    "StackNavigator": {
        "package": ReactNavigation.stack,
        "import": "createNativeStackNavigator",
    },
    "TabNavigator": {
        "package": ReactNavigation.bottom_tabs,
        "import": "createBottomTabNavigator",
    },
    "SafeAreaProvider": {
        "package": "react-native-safe-area-context",
        "import": "SafeAreaProvider",
    },
    **UI_KITTEN_REPLACEMENTS,
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

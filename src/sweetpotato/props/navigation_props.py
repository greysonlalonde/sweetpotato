"""
Provides props for react-navigation components.
"""

NAVIGATION_CONTAINER_PROPS: set = {"children", "ref"}

NATIVE_STACK_NAVIGATOR_PROPS: set = {"name"}

TAB_PROPS: set = {"name"}

BOTTOM_TAB_NAVIGATOR_PROPS: set = {"name"}

DRAWER_NAVIGATOR_PROPS: set = set()

SCREEN_PROPS: set = {
    "children",
    "functions",
    "state",
    "screen_name",
    "state",
    "screen_type",
    "prop_functions",
}

BASE_NAVIGATOR_PROPS: set = set()

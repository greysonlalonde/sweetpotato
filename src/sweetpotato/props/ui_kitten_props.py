"""
Allowed props for ui-kitten components.
"""
ICON_REGISTRY_PROPS: set = {
    "icons"
}  #: Default allowed props for IconRegistry component.

APPLICATION_PROVIDER_PROPS: set = {
    "theme",
    "children",
}  #: Default allowed props for ApplicationProvider component.

LAYOUT_PROPS: set = {
    "children",
    "style",
}  #: Default allowed props for Layout component.

TEXT_PROPS: set = {"text"}  #: Default allowed props for Text component.

BUTTON_PROPS: set = {"title", "onPress"}  #: Default allowed props for Button component.

INPUT_PROPS: set = {
    "placeholder",
    "value",
    "onChangeText",
    "secureTextEntry",
}  #: Default allowed props for Input component.

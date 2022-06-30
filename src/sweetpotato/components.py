"""Abstractions of React Native core components.

See the `React Native docs <https://reactnative.dev/docs/components-and-apis>`_ for more.
"""
from typing import Optional

from sweetpotato.core.base import Component, Composite


class ActivityIndicator(Component):
    """React Native ActivityIndicator component.

    See https://reactnative.dev/docs/activityindicator.
    """

    pass


class Text(Component):
    """React Native Text component.

    See https://reactnative.dev/docs/text.

    Args:
        text: Inner content for Text component inplace of children.
        **kwargs: Arbitrary allowed props for component.
    """

    def __init__(self, text: Optional[str] = None, **kwargs) -> None:
        super().__init__(children=text, **kwargs)


class TextInput(Component):
    """React Native TextInput component.

    See https://reactnative.dev/docs/textinput.
    """

    pass


class Button(Component):
    """React Native Button component.

    See https://reactnative.dev/docs/button.

    Keyword Args:
        title: Title for button.
        **kwargs: Arbitrary allowed props for component.

    Example:
       ``button = Button(title="foo")``
    """

    def __init__(self, title: Optional[str] = None, **kwargs) -> None:
        super().__init__(title, **kwargs)


class Image(Component):
    """React Native Image component.

    See https://reactnative.dev/docs/image.
    """

    pass


class FlatList(Component):
    """React Native FlatList component.

    See https://reactnative.dev/docs/flatlist.
    """

    pass


class SafeAreaProvider(Composite):
    """React Native react-native-safe-area-context SafeAreaProvider component.

    See https://docs.expo.dev/versions/latest/sdk/safe-area-context/.
    """

    pass


class ScrollView(Component):
    """React Native ScrollView component.

    See https://reactnative.dev/docs/scrollview.
    """

    pass


class StyleSheet(Component):
    """React Native StyleSheet component.

    See https://reactnative.dev/docs/stylesheet.

    Todo:
        * Add stylesheet methods.
    """

    def create(self, styles):
        ...


class TouchableOpacity(Composite):
    """React Native TouchableOpacity component.

    See https://reactnative.dev/docs/touchableopacity.
    """

    pass


class View(Composite):
    """React Native View component.

    See https://reactnative.dev/docs/view.
    """

    pass

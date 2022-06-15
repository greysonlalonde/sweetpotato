"""Abstractions of React Native core components.

See the `React Native docs <https://reactnative.dev/docs/components-and-apis>`_ for more.
"""
from typing import Optional

from sweetpotato.config import settings
from sweetpotato.core.base import Component


class View(Component):
    """React Native View component.

    See https://reactnative.dev/docs/view.
    """

    pass


class ActivityIndicator(Component):
    """React Native ActivityIndicator component.

    See https://reactnative.dev/docs/activityindicator.
    """

    pass


class Text(Component):
    """React Native Text component.

    See https://reactnative.dev/docs/text.

    Keyword Args:
        text: Inner content for Text component inplace of children.

    Attributes:
        _text (str): Inner content for Text component inplace of children.

    Todo:
        Look into consolidating text argument as a variation of child.
    """

    def __init__(self, text: Optional[str] = None, **kwargs) -> None:
        self._text = text
        super().__init__(**kwargs)

    def write_component(self) -> str:
        """Overrides Component.write_component method to include text content.

        Returns:
            React Native friendly string representation of component.
        """
        return f"<{self._name} {self._attrs}>{self._text}</{self._name}>"


class Button(Component):
    """React Native Button component.

    See https://reactnative.dev/docs/button.

    Keyword Args:
        title: Title for button.

    Example:
       ``button = Button(title="foo")``
    """

    def __init__(self, **kwargs: str) -> None:
        super().__init__(**kwargs)
        if settings.USE_UI_KITTEN:
            self._children = [Text(text=kwargs.pop("title", ""))]


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


class SafeAreaProvider(Component):
    """React Native-safe-area-context SafeAreaProvider component.

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
        Add stylesheet methods.
    """

    def create(self, styles):
        ...


class TextInput(Component):
    """React Native TextInput component.

    See https://reactnative.dev/docs/textinput.
    """

    pass


class TouchableOpacity(Component):
    """React Native ActivityIndicator component.

    See https://reactnative.dev/docs/touchableopacity.
    """

    pass

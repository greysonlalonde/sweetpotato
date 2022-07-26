"""Abstractions of React Native core components.

See the `React Native docs <https://reactnative.dev/docs/components-and-apis>`_ for more.

Todo:
    * Add Stylesheet class methods.
    * Add examples to all classes.
"""
from typing import Optional

from sweetpotato.config import settings
from sweetpotato.core.base import Component, Composite


class ActivityIndicator(Component):
    """React Native ActivityIndicator component.

    See https://reactnative.dev/docs/activityindicator.
    """


class Text(Component):
    """React Native Text component.

    See https://reactnative.dev/docs/text.

    Args:
        text: Inner content for Text component inplace of children.
        kwargs: Arbitrary allowed props for component.
    """

    def __init__(self, text: Optional[str] = None, **kwargs) -> None:
        super().__init__(children=text, **kwargs)


class TextInput(Component):
    """React Native TextInput component.

    See https://reactnative.dev/docs/textinput.
    """


class Button(Composite):
    """React Native Button component.

    See https://reactnative.dev/docs/button.

    Keyword Args:
        title: Title for button.
        kwargs: Arbitrary allowed props for component.

    Example:
       ``button = Button(title="foo")``
    """

    def __init__(self, **kwargs) -> None:
        title = (
            [Text(text=kwargs.pop("title"))]
            if settings.USE_UI_KITTEN
            else kwargs.update({"title": f"'{kwargs.pop('title', '')}'"})
        )
        if settings.USE_UI_KITTEN:
            kwargs.update({"children": title})
        super().__init__(**kwargs)


class Image(Component):
    """React Native Image component.

    See https://reactnative.dev/docs/image.

    Example:
       ``image = Image(source={"uri": image_source})``
    """


class FlatList(Component):
    """React Native FlatList component.

    See https://reactnative.dev/docs/flatlist.
    """


class SafeAreaProvider(Composite):
    """React Native react-native-safe-area-context SafeAreaProvider component.

    See https://docs.expo.dev/versions/latest/sdk/safe-area-context/.
    """


class ScrollView(Component):
    """React Native ScrollView component.

    See https://reactnative.dev/docs/scrollview.
    """


class StyleSheet(Component):
    """React Native StyleSheet component.

    See https://reactnative.dev/docs/stylesheet.

    Todo:
        * Add stylesheet methods.
        * Add examples.
    """

    def __create(self, styles: dict[str, str]) -> None:
        raise NotImplementedError


class TouchableOpacity(Composite):
    """React Native TouchableOpacity component.

    See https://reactnative.dev/docs/touchableopacity.
    """


class View(Composite):
    """React Native View component.

    See https://reactnative.dev/docs/view.
    """

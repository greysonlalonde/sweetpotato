"""Abstractions of React Native core components.

See the `React Native docs <https://reactnative.dev/docs/components-and-apis>`_ for more.

Todo:
    * Add examples to all classes.
"""
from typing import Optional, Union

from sweetpotato.config import settings
from sweetpotato.core.base import Component, Composite
from sweetpotato.props.components_props import (
    ACTIVITY_INDICATOR_PROPS,
    TEXT_PROPS,
    TEXT_INPUT_PROPS,
    BUTTON_PROPS,
    IMAGE_PROPS,
    FLAT_LIST_PROPS,
    SAFE_AREA_PROVIDER_PROPS,
    SCROLL_VIEW_PROPS,
    TOUCHABLE_OPACITY_PROPS,
    VIEW_PROPS,
)


class ActivityIndicator(Component):
    """React Native ActivityIndicator component.

    See https://reactnative.dev/docs/activityindicator.
    """

    props: set = ACTIVITY_INDICATOR_PROPS


class Text(Component):
    """React Native Text component.

    See https://reactnative.dev/docs/text.

    Args:
        text: Inner content for Text component inplace of children.
        kwargs: Arbitrary allowed props for component.

    Example:
        text = Text(text="foo")
    """

    props: set = TEXT_PROPS

    def __init__(self, text: Optional[str] = None, **kwargs) -> None:
        super().__init__(children=text, **kwargs)


class TextInput(Component):
    """React Native TextInput component.

    See https://reactnative.dev/docs/textinput.
    """

    props: set = TEXT_INPUT_PROPS


class Button(Composite):
    """React Native Button component.

    See https://reactnative.dev/docs/button.

    Keyword Args:
        title: Title for button.
        kwargs: Arbitrary allowed props for component.

    Example:
        button = Button(title="foo")
    """

    props: set = BUTTON_PROPS

    def __init__(self, **kwargs) -> None:
        title = kwargs.update({"title": f"'{kwargs.pop('title', '')}'"})
        if settings.USE_UI_KITTEN:
            kwargs.update({"children": title})
        super().__init__(**kwargs)


class Image(Component):
    """React Native Image component.

    See https://reactnative.dev/docs/image.

    Example:
        image = Image(source={"uri": image_source})
    """

    props: set = IMAGE_PROPS


class FlatList(Component):
    """React Native FlatList component.

    See https://reactnative.dev/docs/flatlist.
    """

    props: set = FLAT_LIST_PROPS


class SafeAreaProvider(Composite):
    """React Native react-native-safe-area-context SafeAreaProvider component.

    See https://docs.expo.dev/versions/latest/sdk/safe-area-context/.
    """

    package: str = "react-native-safe-area-context"
    props: set = SAFE_AREA_PROVIDER_PROPS


class ScrollView(Component):
    """React Native ScrollView component.

    See https://reactnative.dev/docs/scrollview.
    """

    props: set = SCROLL_VIEW_PROPS


class StyleSheet:
    """React Native StyleSheet component.

    See https://reactnative.dev/docs/stylesheet.

    Args:
        styles: Dictionary of dicts consisting of styles.

    Example:
        styles = StyleSheet.create({
            "container": {"flex": 1, "justifyContent": "center", "alignItems": "center"}
        })

    Todo:
        * Implement compose and flatten methods.
    """

    def __init__(self, styles: dict[str, dict[str, Union[str, int]]]) -> None:
        self.styles = styles

    @classmethod
    def create(cls, styles: dict[str, dict[str, Union[str, int]]]) -> "StyleSheet":
        """Method for creating stylesheet for use with components.

        Args:
            styles: Dictionary of dicts consisting of styles.
        """
        return cls(styles)

    def compose(self) -> None:
        """Not implemented."""
        raise NotImplementedError

    def flatten(self) -> None:
        """Not implemented."""
        raise NotImplementedError

    def __getattr__(self, item: str) -> dict:
        return self.styles[item]


class TouchableOpacity(Composite):
    """React Native TouchableOpacity component.

    See https://reactnative.dev/docs/touchableopacity.
    """

    props: set = TOUCHABLE_OPACITY_PROPS


class View(Composite):
    """React Native View component.

    See https://reactnative.dev/docs/view.
    """

    props: set = VIEW_PROPS

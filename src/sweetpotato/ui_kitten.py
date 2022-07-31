"""Contains classes based on UI Kitten components.

See `UI Kitten <https://akveo.github.io/react-native-ui-kitten/docs/components/components-overview>`_
"""
from typing import Optional

from sweetpotato.core.base import Component, Composite
from sweetpotato.props.ui_kitten_props import (
    ICON_REGISTRY_PROPS,
    APPLICATION_PROVIDER_PROPS,
    LAYOUT_PROPS,
    BUTTON_PROPS,
    TEXT_PROPS,
    INPUT_PROPS,
)


class IconRegistry(Component):
    """Implementation of ui-kitten IconRegistry component.

    See `<https://akveo.github.io/react-native-ui-kitten/docs/components/icon/overview#icon>`_
    """

    package: str = "@ui-kitten/components"
    props: set = ICON_REGISTRY_PROPS


class ApplicationProvider(Composite):
    """Implementation of ui-kitten ApplicationProvider component.

    See https://akveo.github.io/react-native-ui-kitten/docs/components/application-provider

    Args:
        kwargs: Arbitrary keyword arguments.
    """

    props: set = APPLICATION_PROVIDER_PROPS
    package: str = "@ui-kitten/components"

    def __init__(self, **kwargs) -> None:
        kwargs.update(
            {
                "children": [
                    IconRegistry(icons="EvaIconsPack"),
                    kwargs.pop("children")[0],
                ]
            }
        )
        super().__init__(**kwargs)

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} {'{'}...eva{'}'}{self.attrs}>{self.children}</{self.__class__.__name__}>"


class Text(Component):
    """Implementation of ui-kitten Text component.

    See https://akveo.github.io/react-native-ui-kitten/docs/components/text.
    """

    props: set = TEXT_PROPS

    def __init__(self, text: Optional[str] = None, **kwargs) -> None:
        super().__init__(children=text, **kwargs)


class Button(Composite):
    """Implementation of ui-kitten Button component.

    See https://akveo.github.io/react-native-ui-kitten/docs/components/button.
    """

    package: str = "@ui-kitten/components"
    props: set = BUTTON_PROPS

    def __init__(self, **kwargs) -> None:
        super().__init__(children=[Text(text=kwargs.pop("title"))], **kwargs)


class Input(Component):
    """Implementation of ui-kitten Input component.

    See https://akveo.github.io/react-native-ui-kitten/docs/components/input.
    """

    package: str = "@ui-kitten/components"
    props: set = INPUT_PROPS


class Layout(Composite):
    """Implementation of ui-kitten Layout component.

    See https://akveo.github.io/react-native-ui-kitten/docs/components/layout.
    """

    package: str = "@ui-kitten/components"
    props: set = LAYOUT_PROPS

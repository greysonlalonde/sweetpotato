"""Contains classes based on UI Kitten components.

See `UI Kitten <https://akveo.github.io/react-native-ui-kitten/docs/components/components-overview>`_
"""
from sweetpotato.core.base import Component, Composite


class IconRegistry(Component):
    """Implementation of ui-kitten IconRegistry component.

    See `<https://akveo.github.io/react-native-ui-kitten/docs/components/icon/overview#icon>`_
    """


class ApplicationProvider(Composite):
    """Implementation of ui-kitten ApplicationProvider component.

    See https://akveo.github.io/react-native-ui-kitten/docs/components/application-provider

    Args:
        kwargs: Arbitrary keyword arguments.
    """

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
        return f"<{self.name} {'{'}...eva{'}'}{self.attrs}>{''.join(map(repr, self._children))}</{self.name}>"


class Layout(Composite):
    """Implementation of ui-kitten Layout component.

    See https://akveo.github.io/react-native-ui-kitten/docs/components/layout.
    """

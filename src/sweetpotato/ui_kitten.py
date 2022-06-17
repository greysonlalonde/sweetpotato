"""Contains classes based on UI Kitten components.

See `UI Kitten <https://akveo.github.io/react-native-ui-kitten/docs/components/components-overview>`_
"""
from abc import ABC, abstractmethod

from sweetpotato.components import Component
from sweetpotato.config import settings


class AbstractUIKitten(ABC):
    """
    Abstraction of Base react-native component.
    """

    @classmethod
    def __init_subclass__(cls):
        required_class_attrs = [
            "_ui_kitten_imports",
        ]
        for attr in required_class_attrs:
            if not hasattr(cls, attr):
                raise NotImplementedError(f"{cls} missing required {attr} attr")

    @classmethod
    @abstractmethod
    def add_ui_kitten(cls):
        """
        Abstract add_ui_kitten method.
        """
        raise NotImplementedError


class UIKitten:
    """Contains UI Kitten package methods."""

    _ui_kitten_imports = {}
    _ui_kitten_component = {}
    _ui_kitten_attrs = {}

    def __init__(self, **kwargs):
        if settings.use_ui_kitten:
            self.add_ui_kitten()
            self.add_imports()
        super().__init__(**kwargs)

    def add_imports(self):
        self._ui_kitten_imports["@eva-design/eva"] = "* as eva"
        self._ui_kitten_attrs = "{...eva}"

    @classmethod
    def add_ui_kitten(cls):
        """
        Adds ui-kitten imports to ApplicationProvider class.
        """
        cls._ui_kitten_component["@ui-kitten/components"] = cls.__name__


class ApplicationProvider(Component, UIKitten):
    """Implementation of ui-kitten ApplicationProvider component.

    See https://akveo.github.io/react-native-ui-kitten/docs/components/application-provider
    Todo:
        * Need to refactor this entirely.
    """

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

        eva = "{...eva}"
        self._attrs = f"{self._attrs} {eva}" if self._attrs else eva


class IconRegistry(Component):
    """Implementation of ui-kitten IconRegistry component.

    ...
    """

    pass


class Layout(Component):
    """Implementation of ui-kitten Layout component.

    See https://akveo.github.io/react-native-ui-kitten/docs/components/layout.
    """

    pass

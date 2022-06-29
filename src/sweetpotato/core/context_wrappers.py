"""
Todo:
    * Add docstrings for all classes & methods.
    * Add typing.
"""
from abc import abstractmethod, ABC
from typing import List

from sweetpotato.authentication import AuthenticationProvider
from sweetpotato.components import SafeAreaProvider
from sweetpotato.config import settings
from sweetpotato.navigation import NavigationContainer
from sweetpotato.ui_kitten import ApplicationProvider


class AbstractWrapper(ABC):
    @abstractmethod
    def set_next(self, wrapper) -> None:
        raise NotImplementedError

    @abstractmethod
    def wrap(self, component) -> None:
        raise NotImplementedError


class Wrapper(AbstractWrapper):
    _next_wrapper: "Wrapper" = None

    def set_next(self, wrapper: "Wrapper") -> None:

        if not self._next_wrapper:
            self._next_wrapper = wrapper
        else:
            self._next_wrapper.set_next(wrapper)

    @abstractmethod
    def wrap(self, component):
        if self._next_wrapper:
            return self._next_wrapper.wrap(component)
        component.is_root = True
        component.is_screen = True
        return component


class UIKittenWrapper(Wrapper):
    def wrap(self, component):
        if settings.USE_UI_KITTEN:
            component = ApplicationProvider(children=[component])
        return super().wrap(component)


class AuthenticationWrapper(Wrapper):
    def wrap(self, component):
        if settings.USE_AUTHENTICATION:
            component = AuthenticationProvider(children=[component])
        return super().wrap(component)


class NavigationWrapper(Wrapper):
    def wrap(self, component):
        if settings.USE_NAVIGATION:
            component = NavigationContainer(children=[component], ref="navigationRef")
        return super().wrap(component)


class ContextWrapper(AuthenticationWrapper, UIKittenWrapper, NavigationWrapper):
    def wrap(self, component: List):
        return super().wrap(SafeAreaProvider(children=component))

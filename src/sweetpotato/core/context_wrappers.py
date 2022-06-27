from abc import abstractmethod, ABC
from typing import List

from sweetpotato.config import settings
from sweetpotato.core.protocols import Composite
from sweetpotato.navigation import NavigationContainer
from sweetpotato.ui_kitten import ApplicationProvider
from sweetpotato.authentication import AuthenticationProvider
from sweetpotato.components import SafeAreaProvider


class Wrapper(ABC):
    @abstractmethod
    def set_next(self, wrapper: "Wrapper") -> "Wrapper":
        raise NotImplementedError

    @abstractmethod
    def wrap(self, component) -> Composite:
        raise NotImplementedError


class AbstractWrapper(Wrapper):
    _next_wrapper: Wrapper = None

    def set_next(self, wrapper: Wrapper) -> Wrapper:
        self._next_wrapper = wrapper
        return wrapper

    @abstractmethod
    def wrap(self, component: Composite) -> Composite:
        if self._next_wrapper:
            return self._next_wrapper.wrap(component)
        component.is_root = True
        return component


class UIKittenWrapper(AbstractWrapper):
    def wrap(self, component: Composite) -> SafeAreaProvider:
        if settings.USE_UI_KITTEN:
            component = ApplicationProvider(children=[component])
        return super().wrap(component)


class AuthenticationWrapper(AbstractWrapper):
    def wrap(self, component: Composite) -> Composite:
        if settings.USE_AUTHENTICATION:
            component = AuthenticationProvider(children=[component])
        return super().wrap(component)


class NavigationWrapper(AbstractWrapper):
    def wrap(self, component: Composite) -> Composite:
        if settings.USE_NAVIGATION:
            component = NavigationContainer(children=[component], ref="navigationRef")
        return super().wrap(component)


class ContextWrapper(AbstractWrapper):
    def __init__(self):
        self.set_next(
            AuthenticationWrapper()
        ).set_next(
            NavigationWrapper()
        ).set_next(
            UIKittenWrapper()
        )

    def wrap(self, component: List) -> Composite:
        component = SafeAreaProvider(children=component)
        context = super().wrap(component)
        print(context)
        return context

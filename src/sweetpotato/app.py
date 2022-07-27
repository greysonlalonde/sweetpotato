"""Provider for React Native entry.

Todo:
    * Add module docstrings
"""
from typing import Optional

from sweetpotato.components import View
from sweetpotato.core.build import Build
from sweetpotato.core.context_wrappers import ContextWrapper
from sweetpotato.core.protocols import CompositeVar, BuildVar, ContextWrapperVar
from sweetpotato.core.utils import ApplicationRenderer


def default_screen() -> CompositeVar:
    """Default welcome screen for application.

    Returns:
        Welcome screen for application.

    Todo:
        * Add actual welcome screen.
    """
    return View()


class App:
    """Provides methods for interacting with underlying :class:`sweetpotato.core.build.Build` class.

    Args:
        component: Top level component, default is the sweetpotato welcome screen.
        context: Context wrapper for application.
        build: Build tools for application.
        theme: Theme of @eva-design/eva, one of dark, light.
        kwargs: Arbitrary keyword arguments.

    Examples:
        `app = App()`
    """

    def __init__(
        self,
        component: Optional[CompositeVar] = None,
        context: Optional[ContextWrapperVar] = None,
        build: Optional[BuildVar] = None,
        theme: Optional[str] = None,
        **kwargs
    ) -> None:
        self._context = ContextWrapper() if not context else context
        self._build = Build() if not build else build
        self._context.wrap(
            component if component else default_screen(), theme=theme, **kwargs
        ).register(renderer=ApplicationRenderer)

    def run(self, platform: Optional[str] = None) -> None:
        """Starts a React Native expo client through a subprocess.

        Args:
            platform: Platform for expo to run application on, one of ios, android, and web.
        """
        self._build.run(platform=platform)

    def publish(self, platform: str) -> None:
        """Publishes app to specified platform / application store.

        Args:
            platform: Platform for app to be published on.
        """
        self._build.publish(platform=platform)

    def show(self) -> str:
        """Returns string .js rendition of application.

        Returns:
            String rendition of application in .js format.
        """
        return self._build.show()

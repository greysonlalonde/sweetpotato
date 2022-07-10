"""Provider for React Native entry.

Todo:
    * Add module docstrings
"""
from typing import Optional

from sweetpotato.core.build import Build
from sweetpotato.core.context_wrappers import ContextWrapper
from sweetpotato.core.protocols import CompositeVar
from sweetpotato.core.utils import ApplicationRenderer


class App:
    """Provides methods for interacting with underlying :class:`sweetpotato.core.build.Build` class.

    Args:
        component (CompositeVar, optional): Top level component.
    """

    _context = ContextWrapper()
    _build = Build()

    def __init__(self, component: Optional[CompositeVar] = None, **kwargs) -> None:
        self._context.wrap(component, **kwargs).register(renderer=ApplicationRenderer)

    def run(self, platform: Optional[str] = None) -> None:
        """Starts a React Native expo client through a subprocess.

        Keyword Args:
            platform (:obj:`str`, optional): Platform for expo to run on.

        Returns:
            None
        """
        self._build.run(platform=platform)

    def publish(self, platform: str) -> None:
        """Publishes app to specified platform / application store.

        Args:
            platform (str): Platform app to be published on.
        """
        self._build.publish(platform=platform)

    def show(self) -> None:
        """Prints .js rendition of application to console.

        Returns:
            None
        """
        print(self._build.show())

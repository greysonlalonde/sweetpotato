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
        children (list): List of components.
    """

    context = ContextWrapper()
    build = Build()

    def __init__(self, children: Optional[list[CompositeVar]] = None, **kwargs) -> None:
        self._context = self.context.wrap(children, **kwargs)
        self._context.register(visitor=ApplicationRenderer)

    def run(self, platform: Optional[str] = None) -> None:
        """Starts a React Native expo client through a subprocess.

        Keyword Args:
            platform (:obj:`str`, optional): Platform for expo to run on.

        Returns:
            None
        """
        self.build.run(platform=platform)

    def publish(self, platform: str) -> None:
        """Publishes app to specified platform / application store.

        Args:
            platform (str): Platform app to be published on.
        """
        self.build.publish(platform=platform)

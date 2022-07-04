from typing import Optional, List

from sweetpotato.core.build import Build
from sweetpotato.core.context_wrappers import ContextWrapper
from sweetpotato.core.utils import (
    ComponentRenderer,
    ApplicationRenderer,
    ImportRenderer,
)


class App:
    """Provides methods for interacting with underlying :class:`sweetpotato.core.build.Build` class.

    Args:
        children (:obj:`list`): List of components.
    """

    context = ContextWrapper()
    build = Build()

    def __init__(self, children: Optional[List] = None, **kwargs) -> None:
        super().__init__()
        if children is None:
            children = []
        self.context = self.context.wrap(children, **kwargs)
        self.context.register(visitor=ComponentRenderer)
        self.context.register(visitor=ImportRenderer)
        self.context.register(visitor=ApplicationRenderer)

    def run(self, platform: Optional[str] = None) -> None:
        """Starts a React Native expo client through a subprocess.

        Keyword Args:
            platform (:obj:`str`, optional: Platform for expo to run on.

        Returns:
            None
        """
        self.build.run(platform=platform)

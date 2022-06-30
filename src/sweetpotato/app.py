from typing import Optional, List

from sweetpotato.config import settings
from sweetpotato.core.build import Build
from sweetpotato.core.context_wrappers import ContextWrapper
from sweetpotato.core.utils import (
    ComponentRenderer,
    ApplicationRenderer,
    ImportRenderer,
    Storage,
)


class App:
    context = ContextWrapper()
    build = Build()

    def __init__(self, children: Optional[List] = None) -> None:
        super().__init__()
        if children is None:
            children = []
        self.context = self.context.wrap(children)
        self.context.register(visitor=ComponentRenderer)
        self.context.register(visitor=ImportRenderer)
        self.context.register(visitor=ApplicationRenderer)
        print(Storage.internals)
        print(settings.REPLACE_COMPONENTS)

    def run(self, platform: Optional[str] = None) -> None:
        """Starts a React Native expo client through a subprocess.

        Keyword Args:
            platform (:obj:`str`, optional: Platform for expo to run on.

        Returns:
            None
        """
        self.build.run(platform=platform)

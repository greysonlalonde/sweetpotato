import subprocess
from typing import Optional, List

from sweetpotato.config import settings
from sweetpotato.core.build import Build
from sweetpotato.core.context_wrappers import ContextWrapper
from sweetpotato.core.utils import (
    Renderer,
    Importer,
    AppProxy,
)

proxy = AppProxy()


class App:
    context = ContextWrapper()
    build = Build()

    def __init__(self, children: Optional[List] = None) -> None:
        super().__init__()
        if children is None:
            children = []
        self.context = self.context.wrap(children)
        self.context.register(visitor=Renderer)
        self.context.register(visitor=Importer)

        l = "{"
        r = "}"
        imports = f"import React from 'react';\n{proxy.internals['App']['imports']}"
        app_repr = f"{imports}export default class App extends React.Component {l} render(){l}return( {self.context.rendition} ){r}{r}"
        with open("App.js", "w") as file:
            file.write(app_repr)

    def run(self, platform: Optional[str] = None) -> None:
        """Starts a React Native expo client through a subprocess.

        Keyword Args:
            platform (:obj:`str`, optional: Platform for expo to run on.

        Returns:
            None
        """
        self.build.run(platform=platform)

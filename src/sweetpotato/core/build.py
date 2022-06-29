"""
The `_access_check` and `_check_dependency` functions are essentially copies from
https://github.com/cookiecutter/whichcraft/blob/master/whichcraft.py#L20.

# npm install -g eas-cli

Todo:
    * Add docstrings for all classes & methods.
    * Add typing.
"""
import sys
import subprocess
import os
from typing import Optional

from sweetpotato.config import settings
from sweetpotato.core.exceptions import DependencyError


def _access_check(fn: str, mode: int) -> bool:
    return os.path.exists(fn) and os.access(fn, mode) and not os.path.isdir(fn)


def _check_dependency(
        cmd: str, mode: int = os.F_OK | os.X_OK, path: Optional[str] = None
) -> Optional[str]:
    if os.path.dirname(cmd):
        if _access_check(cmd, mode):
            return cmd
        return None
    if path is None:
        path = os.environ.get("PATH", os.defpath)
    if not path:
        return None
    path = path.split(os.pathsep)
    if sys.platform == "win32":
        if os.curdir not in path:
            path.insert(0, os.curdir)
        pathext = os.environ.get("PATHEXT", "").split(os.pathsep)
        if any(cmd.lower().endswith(ext.lower()) for ext in pathext):
            files = [cmd]
        else:
            files = [cmd + ext for ext in pathext]
    else:
        files = [cmd]
    seen = set()
    for directory in path:
        norm_dir = os.path.normcase(directory)
        if norm_dir not in seen:
            seen.add(norm_dir)
            for file in files:
                name = os.path.join(directory, file)
                if _access_check(name, mode):
                    return name
    return None


class Build:
    """"""

    def __init__(self, dependencies: list[str] = None) -> None:
        dependencies = dependencies if dependencies else ["npm", "yarn", "expo"]
        for dependency in dependencies:
            if not _check_dependency(dependency):
                raise DependencyError(f"Dependency package {dependency} not found.")

    def write_file(self) -> None:
        """Writes formats all .js files

        Returns:
            None
        """
        with open(
                f"{settings.REACT_NATIVE_PATH}/App.js", "w", encoding="utf-8"
        ) as file:
            file.write("")
        try:
            subprocess.run(
                f"cd {settings.REACT_NATIVE_PATH} && yarn prettier",
                shell=True,
                check=True,
            )
        except subprocess.CalledProcessError as e:
            sys.stdout.write(f"{e}\nTrying yarn install...\n")
            subprocess.run(
                f"cd {settings.REACT_NATIVE_PATH} && yarn install",
                shell=True,
                check=True,
            )

    @staticmethod
    def run(platform: Optional[str] = None) -> None:
        """Starts a React Native expo client through a subprocess.

        Keyword Args:
            platform (:obj:`str`, optional): Platform for expo to run on.

        Returns:
            None
        """
        if not platform:
            platform = ""
        subprocess.run(
            f"cd {settings.REACT_NATIVE_PATH} && expo start {platform}",
            shell=True,
            check=True,
        )

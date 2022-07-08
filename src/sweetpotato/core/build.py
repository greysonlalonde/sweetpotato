"""
The `_access_check` and `_check_dependency` functions are essentially copies from
https://github.com/cookiecutter/whichcraft/blob/master/whichcraft.py#L20.

# npm install -g eas-cli

Todo:
    * Add docstrings for all classes & methods.
    * Add typing.
"""
import os
import subprocess
import sys
from typing import Optional

from sweetpotato.config import settings
from sweetpotato.core.base import DOM


class Build:
    """Contains actions for expo flow, dependency detection, app testing and publishing.

    Args:
        dependencies (:obj:`list`, optional): User defined dependencies to replace inbuilt ones.
    """

    storage = DOM()

    def __init__(self, dependencies: list[str] = None) -> None:
        dependencies = dependencies if dependencies else ["npm", "yarn", "expo"]
        for dependency in dependencies:
            if not self.__check_dependency(dependency):
                raise Exception(f"Dependency package {dependency} not found.")

    @classmethod
    def run(cls, platform: Optional[str] = None) -> None:
        """Starts a React Native expo client through a subprocess.

        Keyword Args:
            platform (:obj:`str`, optional): Platform for expo to run on.

        Returns:
            None
        """

        for screen, content in cls.storage._graph_dict.items():
            content["imports"] = cls.__format_imports(content["imports"])
            cls._write_screen(screen, content)
        cls.__format_screens()
        if not platform:
            platform = ""
        # subprocess.run(
        #     f"cd {settings.REACT_NATIVE_PATH} && expo start {platform}",
        #     shell=True,
        #     check=True,
        # )

    def publish(self, platform: str) -> None:
        """Publishes app to specified platform / application store.

        Args:
            platform (str): Platform app to be published on.
        """
        raise NotImplementedError

    @staticmethod
    def __format_imports(imports_: dict[str, str]) -> str:
        string = ""
        for key, value in imports_.items():
            string += f'import {value} from "{key}";\n'.replace("'", "")
        return string

    @staticmethod
    def __format_screens() -> None:
        """Formats all .js files with prettier.

        Returns:
            None
        """
        try:
            subprocess.run(
                f"cd {settings.REACT_NATIVE_PATH} && yarn prettier",
                shell=True,
                check=True,
            )

        except subprocess.CalledProcessError as error:
            sys.stdout.write(f"{error}\nTrying yarn install...\n")
            subprocess.run(
                f"cd {settings.REACT_NATIVE_PATH} && yarn install",
                shell=True,
                check=True,
            )

    @staticmethod
    def __replace_values(content: dict, screen: str) -> str:
        """Sets placeholder values in the string representation of the app component.

        Args:
            content (dict): Dictionary of screen contents.
            screen (str): Name of screen.

        Returns:
            component (str): String representation of app component with
            placeholder values set.
        """
        component = settings.APP_REPR.replace("<NAME>", screen)
        content.update(dict(state=""))
        if settings.APP_COMPONENT == screen:
            content[
                "imports"
            ] = f"{''.join(settings.APP_IMPORTS)}\n{''.join(content['imports'])}"
            if settings.USE_NAVIGATION:
                content[
                    "imports"
                ] = f"import 'react-native-gesture-handler';\n{''.join(content['imports'])}"
                content["state"] += "navigation: RootNavigation.navigationRef"
        for key in content:
            if key in ["variables", "functions"]:
                content[key] = "\n".join(content[key])

            component = component.replace(f"<{key.upper()}>", str(content[key]))
        return component

    @classmethod
    def _write_screen(cls, screen: str, content: dict) -> None:
        """Writes screen contents to file with screen name as file name.

        Args:
            screen (str): Name of screen.
            content (dict): Dictionary of screen contents.
        """
        component = cls.__replace_values(content, screen)
        if settings.APP_COMPONENT != screen:
            screen = f"src/{screen}"
        with open(
            f"{settings.REACT_NATIVE_PATH}/{screen}.js", "w", encoding="utf-8"
        ) as file:
            file.write(component)

    @staticmethod
    def __access_check(file: str, mode: int) -> bool:
        return (
            os.path.exists(file) and os.access(file, mode) and not os.path.isdir(file)
        )

    @classmethod
    def __check_dependency(
        cls, cmd: str, mode: int = os.F_OK | os.X_OK, path: Optional[str] = None
    ) -> Optional[str]:
        if os.path.dirname(cmd):
            if cls.__access_check(cmd, mode):
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
                    if cls.__access_check(name, mode):
                        return name
        return None

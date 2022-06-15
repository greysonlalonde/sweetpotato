"""Contains general sweetpotato exceptions


"""


class ImproperlyConfigured(Exception):
    """Sweetpotato is somehow improperly configured."""

    pass


class NoChildrenError(Exception):
    """Add a list of child components.

    Args:
        name: Name of component.

    Attributes:
        name (str): Name of component.
    """

    def __init__(self, name: str) -> None:
        self._name = name

    def __str__(self) -> str:
        """Custom __str__ method to show exception message.

        Returns:
            String representation of exception message.
        """
        return f"{self._name} needs children."


class AttrError(Exception):
    """Attribute has incorrect datatype/format.

    Args:
        key: Name of faulty attribute.
        name: Name of component with faulty attribute.

    Attributes:
        _key (str): Name of faulty attribute.
        _name (str): Name of component with faulty attribute.
    """

    def __init__(self, key: str, name: str) -> None:
        self._key = key
        self._name = name

    def __str__(self) -> str:
        """Custom __str__ method to show exception message.

        Returns:
            String representation of exception message.
        """
        return f"attribute '{self._key}' not in {self._name} component props"


class StyleError(Exception):
    """Style has an incorrect key/value for given component."""

    pass


class ScreenError(Exception):
    """Screen has an incorrect key/value or missing arg for given component."""

    pass

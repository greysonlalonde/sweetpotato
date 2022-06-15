import unittest
from sweetpotato.components import FlatList
from sweetpotato.props.components_props import FLAT_LIST_PROPS


class TestFlatList(unittest.TestCase):
    def test_props(self):
        """
        Test that FlatList class props are equal to components_props.py variable.
        """
        self.assertEqual(FlatList._props, FLAT_LIST_PROPS)

    def test_methods(self):
        ...


if __name__ == '__main__':
    unittest.main()

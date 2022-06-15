import unittest
from sweetpotato.components import ScrollView
from sweetpotato.props.components_props import SCROLL_VIEW_PROPS


class TestScrollView(unittest.TestCase):
    def test_props(self):
        """
        Test that ScrollView class props are equal to components_props.py variable.
        """
        scroll_view = ScrollView()
        self.assertTrue(scroll_view._props)
        self.assertEqual(scroll_view._props, SCROLL_VIEW_PROPS)

    def test_has_methods(self):
        """
        Test that ScrollView class has all required methods.
        """
        ...


if __name__ == '__main__':
    unittest.main()

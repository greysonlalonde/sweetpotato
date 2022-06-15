import unittest
from sweetpotato.components import View
from sweetpotato.props.components_props import VIEW_PROPS


class TestView(unittest.TestCase):
    def test_props(self):
        """
        Test that View class props are equal to components_props.py variable.
        """
        view = View()
        self.assertTrue(view._props)
        self.assertEqual(view._props, VIEW_PROPS)

    def test_has_methods(self):
        """
        Test that View class has all required methods.
        """
        ...


if __name__ == '__main__':
    unittest.main()

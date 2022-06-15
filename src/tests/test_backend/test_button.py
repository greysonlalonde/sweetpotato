import unittest
from sweetpotato.components import Button
from sweetpotato.props.components_props import BUTTON_PROPS


class TestButton(unittest.TestCase):
    def test_props(self):
        """
        Test that Button class props are equal to components_props.py variable.
        """
        self.assertEqual(Button._props, BUTTON_PROPS)

    def test_methods(self):
        ...


if __name__ == '__main__':
    unittest.main()

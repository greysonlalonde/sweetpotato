import unittest
from sweetpotato.components import TextInput
from sweetpotato.props.components_props import TEXT_INPUT_PROPS


class TestTextInput(unittest.TestCase):
    def test_props(self):
        """
        Test that TextInput class props are equal to components_props.py variable.
        """
        text_input = TextInput()
        self.assertTrue(text_input._props)
        self.assertEqual(text_input._props, TEXT_INPUT_PROPS)

    def test_has_methods(self):
        """
        Test that TextInput class has all required methods.
        """
        ...


if __name__ == '__main__':
    unittest.main()

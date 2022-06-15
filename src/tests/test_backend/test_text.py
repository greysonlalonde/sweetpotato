import unittest
from sweetpotato.components import Text
from sweetpotato.props.components_props import TEXT_PROPS

phrase = "Hello World"


class TestText(unittest.TestCase):
    def test_props(self):
        """
        Test that Button class props are equal to components_props.py variable.
        """
        text = Text(text=phrase)
        self.assertTrue(text._props)
        self.assertEqual(text._props, TEXT_PROPS)

    def test_has_methods(self):
        """
        Test that Text class has all required methods.
        """
        text = Text(text=phrase)
        self.assertTrue(text.write_component)

    def test_text_attr(self):
        """
        Test that Text class Text._text attr is present and correct.
        """
        text = Text(text=phrase)
        self.assertTrue(text._text)
        self.assertEqual(text._text, phrase)

    def test_write_component(self):
        text = Text(text=phrase)
        self.assertIn(phrase, text.write_component())


if __name__ == '__main__':
    unittest.main()

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
        self.assertTrue(text.props)
        self.assertEqual(text.props, TEXT_PROPS)

    def test_has_methods(self):
        """
        Test that Text class has all required methods.
        """
        text = Text(text=phrase)

    def test_text_attr(self):
        """
        Test that Text class :attr:`Text.children` is present and correct.
        """
        text = Text(text=phrase)
        self.assertEqual(text.children, phrase)

    def test_write_component(self):
        text = Text(text=phrase)


if __name__ == "__main__":
    unittest.main()

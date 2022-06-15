import unittest
from sweetpotato.components import Image
from sweetpotato.props.components_props import IMAGE_PROPS


class TestImage(unittest.TestCase):
    def test_props(self):
        """
        Test that Image class props are equal to components_props.py variable.
        """
        image = Image()
        self.assertTrue(image._props)
        self.assertEqual(image._props, IMAGE_PROPS)

    def test_has_methods(self):
        """
        Test that Image class has all required methods.
        """
        ...


if __name__ == '__main__':
    unittest.main()

import unittest
from sweetpotato.app import App


class TestApp(unittest.TestCase):
    def test_props(self):
        """
        Test that App class props are equal to components_props.py variable.
        """
        app = App()
        self.assertEqual(app._props, {'theme', 'state'})

    def test_has_methods(self):
        """
        Test that App class has all required methods.
        """
        ...


if __name__ == '__main__':
    unittest.main()

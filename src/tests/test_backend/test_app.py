"""Unittests for App class."""
import unittest

from sweetpotato.app import App
from sweetpotato.components import View, Text


class TestApp(unittest.TestCase):

    def setUp(self) -> None:
        """Set up app."""
        component = View(children=[Text(text="Hello, World")])
        self.app_repr = '<SafeAreaProvider ><View ><Text >Hello, World</Text></View></SafeAreaProvider>'
        self.app = App(component=component)

    def test_props(self):
        """
        Test that App class props are equal to components_props.py variable.
        """
        ...

    def test_has_attributes(self):
        ...

    def test_no_component(self):
        App()

    def test_run(self):
        self.assertTrue(self.app.run)

    def test_publish(self):
        self.assertTrue(self.app.publish)

    def test_show(self):
        self.assertIsInstance(str(self.app.show()), str)
        self.assertEqual(str(self.app.show()), self.app_repr)


if __name__ == "__main__":
    unittest.main()

Usage
=====

Creating an app 🧑‍💻
------------------

To create an application, import the :class:`~sweetpotato.app.App` class, give it some child components, and run the app.

For example:

.. code-block:: python

   from sweetpotato.components import View, Text, StyleSheet
   from sweetpotato.app import App

   styles = StyleSheet.create({
        "container": {"flex": 1, "justifyContent": "center", "alignItems": "center"}
   })

   content = View(style=styles.container, children=[Text(text="Hello World")])
   app = App(component=content)

   if __name__ == "__main__":
       app.run()

.. note::

    Styles in React Native differ from ordinary CSS by using camel casing. Check out `this page <https://reactnative.dev/docs/style>`_ for more.


Navigation 🧭
--------------

To use navigation (moving between screens), import a navigator from the navigation module, and pass
your child components as arguments to the :meth:`~sweetpotato.navigation.BaseNavigator.screen` method. Make sure to give each screen a unique name.

.. code-block:: python

    from sweetpotato.navigation import create_bottom_tab_navigator
    from sweetpotato.components import View, Text
    from sweetpotato.app import App

    tab = create_bottom_tab_navigator()

    tab.screen(screen_name="Screen One", children=[View(children=[Text(text="Hello")])])
    tab.screen(screen_name="Screen Two", children=[View(children=[Text(text="World")])])

    app = App(component=tab)

    if __name__ == "__main__":
        app.run()


Design 🎨
----------

Sweetpotato utilizes the React Native `UI Kitten <https://akveo.github.io/react-native-ui-kitten/>`_ framework for quick and aesthetic system design.
To enable it, simply import the :data:`~sweetpotato.config.settings`, set :attr:`~sweetpotato.config.default_settings.Settings.USE_UI_KITTEN`, and use :mod:`~sweetpotato.ui_kitten` components. Make sure to read the UI Kitten documentation
and set a theme for the :class:`~sweetpotato.app.App` class.

Example:

.. code-block:: python

   from sweetpotato.ui_kitten import Layout, Button, Text
   from sweetpotato.config import settings
   from sweetpotato.app import App

   settings.USE_UI_KITTEN = True

   styles = StyleSheet.create({
        "layout": {"flex": 1, "justifyContent": "center", "alignItems": "center"}
   })

   content = Layout(
        style=styles.layout,
        children=[
            Layout(
                children=[
                    Text(
                        text="I am using",
                    ),
                ],
            ),
            Layout(children=[Button(title="UI Kitten")]),
        ]
   )


   app = App(component=content, theme="dark")

   if __name__ == "__main__":
       app.run()



Functions ♻️
-------------
Sweetpotato supports rendering of pure javascript functions. Pass the functions in a list to the top level component.

Example:

.. code-block:: python

   component = View(
       functions=["testFunction = () => {alert('Hello, world')}"],
       children=[Button(title="Press", onPress="() => this.testFunction()")]
   )

   app = App(
       component=component
   )

   if __name__ == "__main__":
       app.run()

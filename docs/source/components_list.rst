Built-in Components 🆓
=======================


react-native
-------------

:class:`~sweetpotato.components.ActivityIndicator`
***************************************

.. code-block:: python

   from sweetpotato.components import ActivityIndicator

   activity_indicator = ActivityIndicator()


:class:`~sweetpotato.components.Button`
***************************************

.. code-block:: python

   from sweetpotato.components import Button

   button = Button(title="Press me", on_press="() => alert('Pressed')")

:class:`~sweetpotato.components.FlatList`
***************************************

.. code-block:: python

   from sweetpotato.components import FlatList

   flat_list = FlatList()

:class:`~sweetpotato.components.Image`
***************************************

.. code-block:: python

   from sweetpotato.components import Button

   image = Image(source={"uri":"your image url"})

:class:`~sweetpotato.components.ScrollView`
***************************************

.. code-block:: python

   from sweetpotato.components import ScrollView

   scroll_view = ScrollView()

:class:`~sweetpotato.components.StyleSheet`
***************************************

.. code-block:: python

   from sweetpotato.components import StyleSheet, View

   styles = StyleSheet.create({
       "container": {"flex": 1, "justifyContent": "center", "alignItems": "center"}
   })
   view = View(style=styles.container)


:class:`~sweetpotato.components.TextInput`
***************************************

.. code-block:: python

   from sweetpotato.components import TextInput

   text_input = TextInput(placeholder="A text component")

:class:`~sweetpotato.components.Text`
***************************************

.. code-block:: python

   from sweetpotato.components import Text

   text = Text(text="A text component")

:class:`~sweetpotato.components.TouchableOpacity`
***************************************

.. code-block:: python

   from sweetpotato.components import TouchableOpacity

   touchable_opacity = TouchableOpacity()

:class:`~sweetpotato.components.View`
***************************************

.. code-block:: python

   from sweetpotato.components import View

   view = View()

@ui-kitten/components
----------------------

:class:`~sweetpotato.ui_kitten.Layout`
***************************************

The UI Kitten equivalent of the :class:`~sweetpotato.components.View` component.

.. code-block:: python

   from sweetpotato.ui_kitten import Layout

   layout = Layout()

:class:`~sweetpotato.ui_kitten.Input`
***************************************

The UI Kitten equivalent of the :class:`~sweetpotato.components.TextInput` component.

.. code-block:: python

   from sweetpotato.ui_kitten import Input

   input_component = Input()


:class:`~sweetpotato.ui_kitten.Button`
***************************************

The UI Kitten equivalent of the :class:`~sweetpotato.components.Button` component.

.. code-block:: python

   from sweetpotato.ui_kitten import Button

   button = Button()


:class:`~sweetpotato.ui_kitten.Text`
***************************************

The UI Kitten equivalent of the :class:`~sweetpotato.components.Text` component.

.. code-block:: python

   from sweetpotato.ui_kitten import Text

   text = Text()


:class:`~sweetpotato.ui_kitten.IconRegistry`
***************************************

In managed mode, sweetpotato handles this component for you.

.. code-block:: python

   from sweetpotato.ui_kitten import IconRegistry

   icon_registry = IconRegistry()

:class:`~sweetpotato.ui_kitten.ApplicationProvider`
***************************************

In managed mode, sweetpotato handles this component for you.

.. code-block:: python

   from sweetpotato.ui_kitten import ApplicationProvider

   application_provider = ApplicationProvider()

@react-navigation
-----------------

:class:`~sweetpotato.navigation.Stack`
************************************************

Rather than instantiating this class directly, use :func:`~sweetpotato.navigation.create_native_stack_navigator`

.. code-block:: python

   from sweetpotato.navigation import create_native_stack_navigator

   stack = create_native_stack_navigator()


:class:`~sweetpotato.navigation.Tab`
**********************************************

Rather than instantiating this class directly, use :func:`~sweetpotato.navigation.create_bottom_tab_navigator`

.. code-block:: python

   from sweetpotato.navigation import create_bottom_tab_navigator

   tab = create_bottom_tab_navigator()


react-native-safe-area-context
-------------------------------

:class:`~sweetpotato.components.SafeAreaProvider`
************************************************

In managed mode, sweetpotato handles this component for you.

.. code-block:: python

   from sweetpotato.components import SafeAreaProvider

   safe_area_provider = SafeAreaProvider()



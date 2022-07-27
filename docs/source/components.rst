Components
==========


react-native
-------------

:class:`~sweetpotato.components.ActivityIndicator`
***************************************

:class:`~sweetpotato.components.Button`
***************************************

:class:`~sweetpotato.components.FlatList`
***************************************

:class:`~sweetpotato.components.Image`
***************************************

:class:`~sweetpotato.components.ScrollView`
***************************************

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

:class:`~sweetpotato.components.Text`
***************************************

:class:`~sweetpotato.components.TouchableOpacity`
***************************************

:class:`~sweetpotato.components.View`
***************************************


@ui-kitten/components
----------

:class:`~sweetpotato.ui_kitten.Layout`
***************************************

The UI Kitten equivalent of the :class:`~sweetpotato.components.View` component.

:class:`~sweetpotato.ui_kitten.IconRegistry`
***************************************

:class:`~sweetpotato.ui_kitten.ApplicationProvider`
***************************************


@react-navigation
-----------


:class:`~sweetpotato.navigation.StackNavigator`
************************************************

Rather than instantiating this class directly, use :func:`~sweetpotato.navigation.create_native_stack_navigator`

.. code-block:: python

   from sweetpotato.navigation import create_native_stack_navigator

   stack = create_native_stack_navigator()


:class:`~sweetpotato.navigation.TabNavigator`
**********************************************

Rather than instantiating this class directly, use :func:`~sweetpotato.navigation.create_bottom_tab_navigator`

.. code-block:: python

   from sweetpotato.navigation import create_bottom_tab_navigator

   tab = create_bottom_tab_navigator()


react-native-safe-area-context
------------------

:class:`~sweetpotato.components.SafeAreaProvider`
************************************************

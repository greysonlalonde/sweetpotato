Components
==========


React Native
-------------

:class:`~sweetpotato.components.Button`
***************************************

:class:`~sweetpotato.components.TextInput`
***************************************

:class:`~sweetpotato.components.Text`
***************************************

:class:`~sweetpotato.components.View`
***************************************


UI Kitten
----------

:class:`~sweetpotato.ui_kitten.Layout`
***************************************

The UI Kitten equivalent of the :class:`~sweetpotato.components.View` component.

:class:`~sweetpotato.ui_kitten.IconRegistry`
***************************************

:class:`~sweetpotato.ui_kitten.ApplicationProvider`
***************************************


Navigation
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

   stack = create_bottom_tab_navigator()

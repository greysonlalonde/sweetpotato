Custom Components 🦄
=====================

Build a Custom Component ⚒️
--------------------------

Instructions for building custom components to be added.


Customizing a component can be as simple as:

.. code-block:: pycon

   >>> from sweetpotato.core.base import RootComponent
   >>> custom_component = RootComponent(name="Name of your component")
   >>> print(custom_component)
   <NameOfYourComponent />

but this doesn't add or change anything, other than the name. For actual customization, read on.

Let's say we want to add our own props to a component.

.. code-block:: python

   from sweetpotato.core.base import RootComponent

   custom_props = {"custom_prop_one", "custom_prop_two"}

   # Name the class something relevant
   class CustomComponent(RootComponent):
       """My first custom component."""
       def __init__(self):
           self.props.update(custom_props)


.. code-block:: pycon

   >>> custom_component = CustomComponent(custom_prop_one="a custom prop")
   >>> print(custom_component)
   <CustomComponent custom_prop_one="a custom prop"/>






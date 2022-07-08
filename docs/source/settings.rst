Settings
========

Application configuration can be customized through settings variables. Default values for these settings are shown at the bottom.

.. note::
   Need to add settings configuration docs.

.. contents:: Table of Contents
   :depth: 1
   :local:



.. setting:: USE_NAVIGATION

``USE_NAVIGATION``
-------------------

**Optional**. Indicated whether to use navigation functionality in app.


.. setting:: USE_UI_KITTEN

``USE_UI_KITTEN``
------------------

**Optional**. Indicated whether to use UI Kitten design functionality in app.


.. setting:: USE_AUTHENTICATION

``USE_AUTHENTICATION``
-----------------------

**Optional**. Indicated whether to use authentication functionality and plugins in app.


.. code-block:: python

     settings.USE_AUTHENTICATION = False
     settings.USE_NAVIGATION = False
     settings.USE_UI_KITTEN = False

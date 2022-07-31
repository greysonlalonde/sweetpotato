Build
=======

Packaging an app 📦
--------------------

1. `Create an expo account <https://expo.dev/signup>`_ if you don't have one.

2. You have two options for building ⚒️:

    a) Do this:

    .. code-block:: python

       # your app logic above^

       # platform may be 'ios', 'android' or 'web'. default is None, build for all.
       # you can also pass `staging='stage'`, where stage = `'production'` or `'preview'`. Defaults to `'preview'`.
       if __name__ == "__main__":
           app.publish(platform="your platform here")


    b) or run these terminal commands in your project directory:

    .. code-block:: console

        (venv) $ eas login
        (venv) $ eas build:configure
        (venv) $ eas build --platform your_platform_here

Distributing the app 📬
------------------------
You can distribute your application through a platform specific app store, or as an internal distribution.
Distribution steps will be added in the near future, but for now visit `<https://docs.expo.dev/build/setup/>`_

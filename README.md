<img src="https://raw.githubusercontent.com/greysonlalonde/sweetpotato/main/media/sweetpotato_github_banner.png" height=25% alt="">

-----
[![alt text](https://img.shields.io/badge/pypi-0.5.a0-blue)](https://pypi.org/project/sweetpotato)
![PyPI - Downloads](https://img.shields.io/pypi/dm/sweetpotato)
[![alt text](https://img.shields.io/badge/license-MIT-green)](https://github.com/greysonlalonde/sweetpotato/blob/main/LICENSE)
[![Documentation Status](https://readthedocs.org/projects/sweetpotato/badge/?version=latest)](https://sweetpotato.readthedocs.io/en/latest/?badge=latest)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

### *This project is still in early stages of development and is not stable.*

Sweetpotato 🥔 provides an intuitive wrapper around [React Native](https://reactnative.dev), making cross-platform
development (iOS, Android, Web)
accessible from Python.

- Supported packages include but are not limited to:
    - [react-native](https://reactnative.dev)
    - [expo](https://expo.dev)
    - [react-navigation](https://reactnavigation.org)
    - [react-native-ui-kitten](https://akveo.github.io/react-native-ui-kitten/)

------

See [https://sweetpotato.readthedocs.io](https://sweetpotato.readthedocs.io) for documentation.

-----
You can view the below example at the following link:
[https://snack.expo.dev/@greysonlalonde13/amused-crackers](https://snack.expo.dev/@greysonlalonde13/amused-crackers)

```python
from sweetpotato.app import App
from sweetpotato.components import Text, Button, Image, StyleSheet
from sweetpotato.ui_kitten import Layout
from sweetpotato.config import settings
from sweetpotato.navigation import create_bottom_tab_navigator

settings.USE_UI_KITTEN = True
settings.USE_NAVIGATION = True

styles = StyleSheet.create({
    "image": {"height": 200, "width": 200, "borderRadius": 50},
    "layout": {
        "justifyContent": "center",
        "alignItems": "center",
        "flex": 1,
    },
    "text": {"margin": 25},
})

tab = create_bottom_tab_navigator(name="tab")

image_url = "https://raw.githubusercontent.com/greysonlalonde/sweetpotato/main/media/sweetpotatoes.JPG"
home_page = Layout(
    style=styles.layout,
    children=[
        Image(style=styles.image, source={"uri": image_url}),
        Text(style=styles.text, text="Sweet, Sweet Potatoes"),
        Button(title="Info", onPress="() => alert('This app was made with sweetpotato')")
    ]
)

tab.screen(
    screen_name="Home",
    children=[home_page],
)
app = App(component=tab, theme="dark")

if __name__ == "__main__":
    app.run()

```

iOS, Android, and web:
<img src="https://raw.githubusercontent.com/greysonlalonde/sweetpotato/main/media/sweetpotato_readme_example.jpg" width=100% height=25% alt="">

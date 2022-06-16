<img src="https://raw.githubusercontent.com/greysonlalonde/sweetpotato/main/media/sweetpotato_github_banner.png" height=25% alt="">

-----
[![alt text](https://img.shields.io/badge/pypi-0.1.a0-blue)](https://pypi.org/project/sweetpotato) [![alt text](https://img.shields.io/badge/license-MIT-green)](https://github.com/greysonlalonde/sweetpotato/blob/main/LICENSE) [![Documentation Status](https://readthedocs.org/projects/sweetpotato/badge/?version=latest)](https://sweetpotato.readthedocs.io/en/latest/?badge=latest)


### *This project is still in early stages of development.*

Sweetpotato provides an intuitive wrapper around React Native, making cross-platform development accessible from Python.
- Supported packages:
  - [react-native](https://reactnative.dev)
  - [expo](https://expo.dev)
  - [react-navigation](https://reactnavigation.org)
  - [react-native-ui-kitten](https://akveo.github.io/react-native-ui-kitten/)
------

See [https://sweetpotato.readthedocs.io](https://sweetpotato.readthedocs.io) for documentation.

-----
Simple example:

```python
from sweetpotato.app import App
from sweetpotato.components import (
    View, 
    Text,
)

app = App(
    children=[
        View(
            style={"justifyContent": "center", "alignItems": "center", "height": "100%"},
            children=[
                Text(text="Hello World")
            ],
        )
    ]
)


if __name__ == "__main__":
    app.run()                
```
<img src="https://raw.githubusercontent.com/greysonlalonde/sweetpotato/main/media/readme_example.png?token=GHSAT0AAAAAABRVMLYCCZOSMGMRDYIRP4QCYSYUQRA" width=25% height=25% alt="">

Navigation example:
```python
from sweetpotato.app import App
from sweetpotato.navigation import TabNavigator
from sweetpotato.components import (
  View, 
  Text,
)

tab = TabNavigator()

tab.screen(screen_name="Screen One", children=[View(children=[Text(text="Hello")])])
tab.screen(screen_name="Screen Two", children=[View(children=[Text(text="World")])])

app = App(children=[tab])

if __name__ == "__main__":
    app.run()
```



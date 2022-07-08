from sweetpotato.app import App
from sweetpotato.components import Text, Button, View
from sweetpotato.config import settings
from sweetpotato.navigation import create_bottom_tab_navigator

settings.USE_UI_KITTEN = True
settings.USE_NAVIGATION = True

view_style = {
    "height": "100%", "justifyContent": "center",
    "alignItems": "center", "flex": 1,
}

tab = create_bottom_tab_navigator(name="tab")
tab.screen(
    screen_name="Screen One",
    children=[View(children=[Text(text="Hello"), Button(title="Press me")], style=view_style)]
)
tab.screen(
    screen_name="Screen Two",
    children=[View(children=[Text(text="World")], style=view_style)]
)
app = App(children=[tab], theme="dark", state={"authenticated": False})

if __name__ == "__main__":
    app.run()

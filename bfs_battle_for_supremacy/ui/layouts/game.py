from ui.root.layout import Layout
from ui.root.button import Button
from ui.root.center import Center
from ui.utils import get_font
from config import WIDTH, HEIGHT


class Game(Layout):
    def setup_components(self):
        self.button = Button(
            0,
            0,
            100,
            100,
            "red",
            "blue",
            "draw",
            get_font(30),
        )

        self.add_component(Center(0, 0, WIDTH, HEIGHT, self.button))

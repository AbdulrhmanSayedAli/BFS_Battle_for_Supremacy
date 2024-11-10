from ui.root.layout import Layout
from ui.root.button import Button
from ui.root.image import Image
from ui.root.text import Text
from ui.root.rectangle import Rectangle
from ui.utils import get_font
from config import WIDTH, HEIGHT, IMAGES_PATH


class MainMenu(Layout):
    def setup_components(self):
        button = Button(
            10,
            10,
            200,
            100,
            color="red",
            secondary_color="blue",
            text="click me here",
            font=get_font(40),
        )

        def d(c, event):
            c.x += 10
            c.y += 10

        button.on_click = d

        background = Image(
            0, 0, WIDTH, HEIGHT, IMAGES_PATH + "main_menu_background.webp"
        )

        blur = Rectangle(0, 0, WIDTH, HEIGHT, background_color=(0, 0, 0, 140))

        text = Text(500, 100, "red", "blue", "Hi this is a text", get_font(40))

        self.add_component(background)
        self.add_component(blur)
        self.add_component(button)
        self.add_component(text)
        super().setup_components()

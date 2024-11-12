from ui.root.layout import Layout
from ui.root.button import Button
from ui.root.image import Image
from ui.root.rectangle import Rectangle
from ui.root.center import Center
from ui.root.container import Container
from ui.utils import get_font, main_color, main_color_hover
from config import WIDTH, HEIGHT, IMAGES_PATH
from ui.root.dialog import Dialog


class MainMenu(Layout):

    def on_quit_clicked(button, event):
        pass

    def setup_components(self):
        self.start_button = Button(
            0,
            0,
            200,
            100,
            color=main_color,
            secondary_color=main_color_hover,
            text="Start",
            font=get_font(40),
            border_radius=10,
        )

        self.options_button = Button(
            0,
            120,
            200,
            100,
            color=main_color,
            secondary_color=main_color_hover,
            text="Options",
            font=get_font(40),
            border_radius=10,
        )

        self.quit_button = Button(
            0,
            240,
            200,
            100,
            color=main_color,
            secondary_color=main_color_hover,
            text="Quit",
            font=get_font(40),
            border_radius=10,
        )

        self.dialog = Dialog(
            "title",
            "Some message",
            background_color="white",
            on_ok=lambda: self.remove_component(self.dialog),
        )

        self.add_component(
            Image(
                0, 0, WIDTH, HEIGHT, IMAGES_PATH + "main_menu_background.webp"
            )
        )
        self.add_component(
            Rectangle(0, 0, WIDTH, HEIGHT, background_color=(0, 0, 0, 140))
        )
        self.add_component(
            Center(
                0,
                0,
                WIDTH,
                HEIGHT,
                Container(
                    0,
                    0,
                    200,
                    340,
                    [self.start_button, self.options_button, self.quit_button],
                ),
            )
        )
        self.add_component(self.dialog)

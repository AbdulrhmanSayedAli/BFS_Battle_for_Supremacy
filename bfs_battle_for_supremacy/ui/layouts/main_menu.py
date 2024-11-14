from bfs_battle_for_supremacy.ui.root import (
    Layout,
    Button,
    Image,
    Rectangle,
    Center,
    Container,
    Dialog,
)
from bfs_battle_for_supremacy.ui.utils import (
    get_font,
    main_color,
    main_color_hover,
)
from bfs_battle_for_supremacy.config import WIDTH, HEIGHT, IMAGES_PATH
from bfs_battle_for_supremacy.ui.engine import Engine
import os


class MainMenu(Layout):

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
            on_click=lambda c, e: Engine.navigate(1),
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
            on_click=lambda c, e: self.add_component(self.quit_dialog),
        )

        def quit_dialog_ok():
            self.remove_component(self.quit_dialog)
            Engine.running = False

        self.quit_dialog = Dialog(
            "Warning",
            "Are you sure you want to exit?",
            background_color="white",
            on_ok=quit_dialog_ok,
            on_cancel=lambda: self.remove_component(self.quit_dialog),
        )

        self.add_component(
            Image(
                0,
                0,
                WIDTH,
                HEIGHT,
                os.path.join(IMAGES_PATH, "main_menu_background.webp"),
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

        self.add_component(
            Rectangle(15, 15, 110, 110, background_color="white")
        )
        self.add_component(
            Image(20, 20, 100, 100, os.path.join(IMAGES_PATH, "icon.webp"))
        )

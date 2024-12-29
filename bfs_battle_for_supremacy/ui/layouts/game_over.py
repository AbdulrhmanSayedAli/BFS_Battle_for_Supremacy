from bfs_battle_for_supremacy.game_logic.managers.player_manager import PlayerManager
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
from bfs_battle_for_supremacy.ui.root.text import Text

class GameOver(Layout):

    def setup_components(self):
        self.text = Text(0,
                         0,
                         "Red",
                         "Red",
                         text="Player1 has lost",
                         font=get_font(30),
                         width=230,
                         height=100
                         )
        self.start_button = Button(
            0,
            100,
            200,
            100,
            color=main_color,
            secondary_color=main_color_hover,
            text="Ok",
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
                    240,
                    400,
                    [self.text, self.start_button],
                ),
            )
        )

        self.add_component(
            Rectangle(15, 15, 110, 110, background_color="white")
        )
        self.add_component(
            Image(20, 20, 100, 100, os.path.join(IMAGES_PATH, "icon.webp"))
        )
    def update_components(self):
        lost1=PlayerManager.players[0].has_lost
        lost2=PlayerManager.players[1].has_lost
        if lost1:
            self.text.text="Player1 has lost"
        if lost2:
            self.text.text="Player2 has lost"
        
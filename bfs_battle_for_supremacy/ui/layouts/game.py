from ui.root.layout import Layout
from ui.root.button import Button
from ui.components.game.board import Board
from ui.utils import get_font
from config import WIDTH
from ui.utils import main_color, main_color_hover

BOARD_WIDTH = 700
BOARD_HEIGHT = 700
SELECTION_WIDTH = 500
SELECTION_HEIGHT = 400
STATS_WIDTH = 500
STATS_HEIGHT = 200


class Game(Layout):
    def setup_components(self):
        self.board: Board = Board(0, 0, BOARD_WIDTH, BOARD_HEIGHT)

        self.selection = Button(
            BOARD_WIDTH,
            0,
            SELECTION_WIDTH,
            SELECTION_HEIGHT,
            "yellow",
            "yellow",
            "select something",
            get_font(40),
            font_color="black",
        )

        self.stats = [
            Button(
                BOARD_WIDTH,
                SELECTION_HEIGHT,
                STATS_WIDTH / 2,
                STATS_HEIGHT,
                "red",
                "red",
                "player 1 stats",
                get_font(20),
            ),
            Button(
                BOARD_WIDTH + STATS_WIDTH / 2,
                SELECTION_HEIGHT,
                STATS_WIDTH / 2,
                STATS_HEIGHT,
                "blue",
                "blue",
                "player 2 stats",
                get_font(20),
            ),
        ]

        self.draw_card_button = Button(
            BOARD_WIDTH + 40,
            SELECTION_HEIGHT + STATS_HEIGHT + 10,
            120,
            80,
            main_color,
            main_color_hover,
            "draw card",
            get_font(30),
            border_radius=10,
        )

        self.end_turn_button = Button(
            WIDTH - 160,
            SELECTION_HEIGHT + STATS_HEIGHT + 10,
            120,
            80,
            main_color,
            main_color_hover,
            "end turn",
            get_font(30),
            border_radius=10,
        )

        self.add_component(self.board)
        self.add_component(self.stats[0])
        self.add_component(self.stats[1])
        self.add_component(self.selection)
        self.add_component(self.draw_card_button)
        self.add_component(self.end_turn_button)

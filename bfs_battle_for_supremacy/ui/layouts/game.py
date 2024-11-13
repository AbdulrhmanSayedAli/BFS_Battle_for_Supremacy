from ui.root.layout import Layout
from ui.root.button import Button
from ui.root.center import Center
from ui.components.game.board import Board
from ui.components.game.tile import Tile
from ui.utils import get_font
from config import BOARD_SIZE_WIDTH, BOARD_SIZE_HEIGHT, IMAGES_PATH

BOARD_WIDTH = 700
BOARD_HEIGHT = 700
SELECTION_WIDTH = 500
SELECTION_HEIGHT = 400
STATS_WIDTH = 500
STATS_HEIGHT = 200


class Game(Layout):
    def setup_tiles(self, width, height) -> list[list[Tile]]:
        tile_height = height / BOARD_SIZE_HEIGHT
        tile_width = width / BOARD_SIZE_WIDTH
        res: list[list[Tile]] = []
        for i in range(BOARD_SIZE_HEIGHT):
            cur_res: list[Tile] = []
            for j in range(BOARD_SIZE_WIDTH):
                cur_res.append(
                    Tile(
                        j * tile_width,
                        i * tile_height,
                        tile_width,
                        tile_height,
                        j,
                        i,
                    )
                )
            res.append(cur_res)
        res[0][0].image_path = IMAGES_PATH + "player1.webp"
        res[BOARD_SIZE_HEIGHT - 1][BOARD_SIZE_WIDTH - 1].image_path = (
            IMAGES_PATH + "player2.webp"
        )
        return res

    def setup_components(self):

        self.tiles: list[list[Tile]] = self.setup_tiles(
            BOARD_WIDTH, BOARD_HEIGHT
        )
        self.board: Board = Board(0, 0, BOARD_WIDTH, BOARD_HEIGHT, self.tiles)

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
                "blue",
                "blue",
                "player 1 stats",
                get_font(20),
            ),
            Button(
                BOARD_WIDTH + STATS_WIDTH / 2,
                SELECTION_HEIGHT,
                STATS_WIDTH / 2,
                STATS_HEIGHT,
                "red",
                "red",
                "player 2 stats",
                get_font(20),
            ),
        ]

        self.add_component(self.board)
        self.add_component(self.stats[0])
        self.add_component(self.stats[1])
        self.add_component(self.selection)

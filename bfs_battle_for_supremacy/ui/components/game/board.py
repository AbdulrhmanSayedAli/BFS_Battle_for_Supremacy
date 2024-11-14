from typing import Callable
from ui.root.container import Container
from ui.components.game.tile import Tile
from config import BOARD_SIZE_WIDTH, BOARD_SIZE_HEIGHT, IMAGES_PATH


class Board(Container):
    def __init__(
        self,
        x: float,
        y: float,
        width: float,
        height: float,
        on_click: Callable = None,
        on_hover: Callable = None,
        on_hover_end: Callable = None,
    ):
        self._tiles = self.setup_tiles(width, height)
        components = [tile for row in self.tiles for tile in row]
        super().__init__(
            x, y, width, height, components, on_click, on_hover, on_hover_end
        )

    @property
    def tiles(self) -> list[list[Tile]]:
        return self._tiles

    @tiles.setter
    def tiles(self, tiles):
        self._tiles = tiles
        self.components = [tile for row in tiles for tile in row]

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
                        on_click=lambda c, e: self.select_tile(c.pos),
                    )
                )
            res.append(cur_res)
        res[0][0].image_path = IMAGES_PATH + "player1.webp"
        res[BOARD_SIZE_HEIGHT - 1][BOARD_SIZE_WIDTH - 1].image_path = (
            IMAGES_PATH + "player2.webp"
        )
        return res

    def select_tile(self, pos):
        tile: Tile = self.components[pos]
        if tile.selected:
            self.tiles[tile.pos_y][tile.pos_x].selected = False
            return
        for i in range(len(self.tiles)):
            for j in range(len(self.tiles[i])):
                self.tiles[i][j].selected = False
        self.tiles[tile.pos_y][tile.pos_x].selected = True

from typing import Callable
from ui.root.container import Container
from ui.components.game.tile import Tile


class Board(Container):
    def __init__(
        self,
        x: float,
        y: float,
        width: float,
        height: float,
        tiles: list[list[Tile]],
        on_click: Callable = None,
        on_hover: Callable = None,
        on_hover_end: Callable = None,
    ):
        components = [tile for row in tiles for tile in row]
        super().__init__(
            x, y, width, height, components, on_click, on_hover, on_hover_end
        )

    def select_tile(self, pos):
        if self.components[pos].selected:
            self.components[pos].selected = False
            return
        for i in range(len(self.components)):
            self.components[i].selected = False
        self.components[pos].selected = True

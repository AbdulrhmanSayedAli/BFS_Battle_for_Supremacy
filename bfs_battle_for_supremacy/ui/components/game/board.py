from typing import Callable
from bfs_battle_for_supremacy.ui.root.component import Component
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

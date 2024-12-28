from typing import Callable
from pygame.event import Event
from bfs_battle_for_supremacy.ui.root import Component, Image
from bfs_battle_for_supremacy.ui.utils import (
    tile_main_color,
    tile_secondary_color,
)
from bfs_battle_for_supremacy.config import BOARD_SIZE_WIDTH
from bfs_battle_for_supremacy.game_logic.entities.square import Square


class Tile(Component):
    def __init__(
        self,
        x: float,
        y: float,
        width: float,
        height: float,
        pos_x: int,
        pos_y: int,
        square: Square,
        selected: bool = False,
        image_path: str = None,
        on_click: Callable = None,
        on_hover: Callable = None,
        on_hover_end: Callable = None,
    ):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.selected = selected
        self._image_path = image_path
        self.square = square
        self.image: Image = None
        if self._image_path:
            self.image = Image(
                5,
                5,
                width - 10,
                height - 10,
                self._image_path,
            )
        super().__init__(
            x,
            y,
            width,
            height,
            on_click,
            on_hover,
            on_hover_end,
        )

    @property
    def image_path(self):
        return self._image_path

    @image_path.setter
    def image_path(self, value):
        if value:
            self._image_path = value
            self.image = Image(
                5, 5, self.rect.width - 10, self.rect.height - 10, value
            )
        else:
            self.image = None

    @property
    def pos(self):
        return BOARD_SIZE_WIDTH * self.pos_y + self.pos_x

    @property
    def board_color(self):
        if self.selected:
            return (227, 135, 109)

        return (
            tile_main_color
            if (self.pos + self.pos_y) % 2 == 0
            else tile_secondary_color
        )

    def draw(self, screen):
        self.fill(self.board_color)
        if self.image:
            self.image.draw(self)
        screen.blit(self, self.rect.topleft)

    def _on_hover_listener(self, event: Event):
        self.background_color = (156, 156, 156)
        return super()._on_hover_listener(event)

    def _on_hover_end_listener(self, event: Event):
        self.background_color = self.board_color
        return super()._on_hover_end_listener(event)

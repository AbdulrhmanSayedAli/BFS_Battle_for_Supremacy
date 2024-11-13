from typing import Callable
from pygame.event import Event
from ui.root.rectangle import Rectangle
from ui.root.image import Image
from ui.utils import tile_main_color, tile_secondary_color
from config import BOARD_SIZE_HEIGHT


class Tile(Rectangle):
    def __init__(
        self,
        x: float,
        y: float,
        width: float,
        height: float,
        pos_x: int,
        pos_y: int,
        image_path: str = None,
        on_click: Callable = None,
        on_hover: Callable = None,
        on_hover_end: Callable = None,
    ):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self._image_path = image_path
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
            self.board_color,
            on_click,
            on_hover,
            on_hover_end,
        )

    @property
    def image_path(self):
        return self._image_path

    @image_path.setter
    def image_path(self, value):
        self._image_path = value
        self.image = Image(0, 0, self.rect.width, self.rect.height, value)

    @property
    def pos(self):
        return BOARD_SIZE_HEIGHT * self.pos_y + self.pos_x

    @property
    def board_color(self):
        return (
            tile_main_color
            if (self.pos + self.pos_y) % 2 == 0
            else tile_secondary_color
        )

    def draw(self, screen):
        self.fill(self.background_color)
        if self.image:
            self.image.draw(self)
        screen.blit(self, self.rect.topleft)

    def _on_hover_listener(self, event: Event):
        self.background_color = (156, 156, 156)
        return super()._on_hover_listener(event)

    def _on_hover_end_listener(self, event: Event):
        self.background_color = self.board_color
        return super()._on_hover_end_listener(event)

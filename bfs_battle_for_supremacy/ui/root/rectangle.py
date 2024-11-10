from ui.root.component import Component
from typing import Callable


class Rectangle(Component):
    def __init__(
        self,
        x: float,
        y: float,
        width: float,
        height: float,
        background_color=(0, 0, 0, 0),
        on_click: Callable = None,
        on_hover: Callable = None,
        on_hover_end: Callable = None,
    ):
        super().__init__(x, y, width, height, on_click, on_hover, on_hover_end)
        self.background_color = background_color

    def draw(self, screen):
        self.fill(self.background_color)
        return super().draw(screen)

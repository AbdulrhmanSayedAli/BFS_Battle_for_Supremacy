from typing import Callable
from ui.root.component import Component
import pygame


class Container(Component):
    def __init__(
        self,
        x: float,
        y: float,
        width: float,
        height: float,
        components: list[Component],
        on_click: Callable = None,
        on_hover: Callable = None,
        on_hover_end: Callable = None,
    ):
        super().__init__(x, y, width, height, on_click, on_hover, on_hover_end)
        self.components = components

    def draw(self, screen: pygame.Surface):
        self.fill((0, 0, 0, 0))
        for component in self.components:
            component.draw(self)
        super().draw(screen)

    def handle_mouse_event(self, event: pygame.event.Event):
        super().handle_mouse_event(event)
        for component in self.components:
            component.handle_mouse_event(event)

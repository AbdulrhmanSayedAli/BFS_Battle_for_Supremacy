from typing import Callable
from ui.root.component import Component
import pygame


class Center(Component):
    def __init__(
        self,
        x: float,
        y: float,
        width: float,
        height: float,
        component: Component,
        on_click: Callable = None,
        on_hover: Callable = None,
        on_hover_end: Callable = None,
    ):
        super().__init__(x, y, width, height, on_click, on_hover, on_hover_end)
        self.component = component
        new_x = (
            self.x + (self.rect.width / 2) - (self.component.rect.width / 2)
        )
        new_y = (
            self.y + (self.rect.height / 2) - (self.component.rect.height / 2)
        )

        self.component.x += new_x
        self.component.y += new_y

    def draw(self, screen: pygame.Surface):
        self.fill((0, 0, 0, 0))
        self.component.draw(self)
        super().draw(screen)

    def handle_mouse_event(self, event: pygame.event.Event):
        super().handle_mouse_event(event)
        self.component.handle_mouse_event(event)

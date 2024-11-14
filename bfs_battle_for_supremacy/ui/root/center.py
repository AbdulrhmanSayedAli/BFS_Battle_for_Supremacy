from typing import Callable
from bfs_battle_for_supremacy.ui.root.component import Component
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
        self.component = component
        new_x = x + (width / 2) - (self.component.rect.width / 2)
        new_y = y + (height / 2) - (self.component.rect.height / 2)

        self.component.x += new_x
        self.component.y += new_y

        super().__init__(x, y, width, height, on_click, on_hover, on_hover_end)

    def draw(self, screen: pygame.Surface):
        self.fill((0, 0, 0, 0))
        self.component.draw(self)
        super().draw(screen)

    def handle_mouse_event(
        self,
        event: pygame.event.Event,
        rect: pygame.Rect = pygame.Rect(0, 0, 0, 0),
    ):
        super().handle_mouse_event(event)
        self.component.handle_mouse_event(
            event, self.merge_rects(self.rect, rect)
        )

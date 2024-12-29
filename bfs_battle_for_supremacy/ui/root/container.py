from typing import Callable
from bfs_battle_for_supremacy.ui.root.component import Component
import pygame


class Container(Component):
    def __init__(
        self,
        x: float,
        y: float,
        width: float,
        height: float,
        components: list[Component],
        color=(0, 0, 0, 0),
        on_click: Callable = None,
        on_hover: Callable = None,
        on_hover_end: Callable = None,
    ):
        print("constructor: ", color)
        super().__init__(x, y, width, height, on_click, on_hover, on_hover_end)
        self.components = components
        self.color = color

    def draw(self, screen: pygame.Surface):
        if self.color:
            self.fill(self.color)
        for component in self.components:
            component.draw(self)
        super().draw(screen)

    def handle_mouse_event(
        self,
        event: pygame.event.Event,
        rect: pygame.Rect = pygame.Rect(0, 0, 0, 0),
    ):
        super().handle_mouse_event(event)
        for component in self.components:
            component.handle_mouse_event(
                event, self.merge_rects(self.rect, rect)
            )

from ui.root.component import Component
from pygame.event import Event
from typing import Callable
import pygame


class Text(Component):
    def __init__(
        self,
        x: float,
        y: float,
        color,
        secondary_color,
        text: str,
        font: pygame.font.Font,
        width: float = None,
        height: float = None,
        background_color=None,
        on_click: Callable = None,
        on_hover: Callable = None,
        on_hover_end: Callable = None,
    ):

        self.color = color
        self.secondary_color = secondary_color
        self.background_color = background_color
        self.text = text
        self.font = font
        text_surf = font.render(text, True, color)
        width = width or text_surf.get_size()[0]
        height = height or text_surf.get_size()[1]

        super().__init__(
            x,
            y,
            width,
            height,
            on_click,
            on_hover,
            on_hover_end,
        )

    def draw(self, screen: pygame.Surface):
        text_surf = self.font.render(self.text, True, self.color)
        if self.background_color:
            self.fill(self.background_color)

        self.blit(text_surf, (0, 0))
        super().draw(screen)

    def _on_hover_listener(self, event: Event):
        self.color, self.secondary_color = self.secondary_color, self.color
        super()._on_hover_listener(event)

    def _on_hover_end_listener(self, event: Event):
        self.color, self.secondary_color = self.secondary_color, self.color
        super()._on_hover_listener(event)

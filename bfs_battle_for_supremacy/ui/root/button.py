from pygame.event import Event
from ui.root.component import Component
from typing import Callable
import pygame


class Button(Component):
    def __init__(
        self,
        x: float,
        y: float,
        width: float,
        height: float,
        color,
        secondary_color,
        text: str,
        font: pygame.font.Font,
        font_color="white",
        on_click: Callable = None,
        on_hover: Callable = None,
        on_hover_end: Callable = None,
    ):
        super().__init__(
            x,
            y,
            width,
            height,
            on_click,
            on_hover,
            on_hover_end,
        )
        self.color = color
        self.secondary_color = secondary_color
        self.font_color = font_color
        self.text = text
        self.font = font

    def draw(self, screen: pygame.Surface):
        self.fill(self.color)

        text_surf = self.font.render(self.text, True, self.font_color)
        text_rect = text_surf.get_rect(
            center=(self.rect.width // 2, self.rect.height // 2)
        )
        self.blit(text_surf, text_rect)

        super().draw(screen)

    def _on_hover_listener(self, event: Event):
        self.color, self.secondary_color = self.secondary_color, self.color
        super()._on_hover_listener(event)

    def _on_hover_end_listener(self, event: Event):
        self.color, self.secondary_color = self.secondary_color, self.color
        super()._on_hover_listener(event)

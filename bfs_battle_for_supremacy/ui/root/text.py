from bfs_battle_for_supremacy.ui.root.component import Component
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
        background_color=(0, 0, 0, 0),
        on_click: Callable = None,
        on_hover: Callable = None,
        on_hover_end: Callable = None,
    ):
        self.color = color
        self.secondary_color = secondary_color
        self.background_color = background_color
        self._text = text
        self.font = font
        self.line_spacing = 5
        self.text_lines = []

        text_surf = font.render(text, True, color)
        width = width or text_surf.get_width()

        self.width = width
        self.split_text_into_lines()

        line_height = self.font.get_linesize()
        height = height or (
            line_height * len(self.text_lines)
            + (len(self.text_lines) - 1) * self.line_spacing
        )
        self.height = height

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
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        self._text = value
        self = self.__init__(
            self.x,
            self.y,
            self.color,
            self.secondary_color,
            self.text,
            self.font,
            self.width,
            self.height,
            self.background_color,
            self.on_click,
            self.on_hover,
            self.on_hover_end,
        )

    def split_text_into_lines(self):
        """Splits the text into lines that fit within the specified width."""
        chars = self._text
        line = ""
        self.text_lines = []

        for char in chars:
            test_line = line + char
            test_surf = self.font.render(test_line, True, self.color)

            if test_surf.get_width() <= self.width:
                line = test_line
            else:
                self.text_lines.append(line.strip())
                line = char

        if line:
            self.text_lines.append(line.strip())

    def draw(self, screen: pygame.Surface):
        if self.background_color:
            self.fill(self.background_color)

        y_offset = 0
        for line in self.text_lines:
            text_surf = self.font.render(line, True, self.color)
            self.blit(text_surf, (0, y_offset))
            y_offset += self.font.get_linesize() + self.line_spacing

        super().draw(screen)

    def _on_hover_listener(self, event: Event):
        self.color, self.secondary_color = self.secondary_color, self.color
        super()._on_hover_listener(event)

    def _on_hover_end_listener(self, event: Event):
        self.color, self.secondary_color = self.secondary_color, self.color
        super()._on_hover_listener(event)

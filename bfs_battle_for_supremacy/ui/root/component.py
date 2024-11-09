import pygame
from typing import Callable
from ui.root.mouse_event_handler import MouseEventHandler


class Component(pygame.Surface, MouseEventHandler):
    def __init__(
        self,
        x: float,
        y: float,
        width: float,
        height: float,
        on_click: Callable = None,
        on_hover: Callable = None,
        on_hover_end: Callable = None,
    ):
        pygame.Surface.__init__(self, (width, height))

        self._x = x
        self._y = y
        self.rect = self.get_rect(topleft=(self._x, self._y))

        MouseEventHandler.__init__(
            self,
            self.rect,
            on_click=on_click,
            on_hover=on_hover,
            on_hover_end=on_hover_end,
        )

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value
        self.rect.x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value
        self.rect.y = value

    def draw(self, screen: pygame.Surface):
        screen.blit(self, self.rect.topleft)

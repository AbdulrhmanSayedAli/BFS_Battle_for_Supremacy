import pygame
from typing import Callable
from bfs_battle_for_supremacy.ui.root.component import Component


class Image(Component):
    def __init__(
        self,
        x: float,
        y: float,
        width: float,
        height: float,
        image_path: str,
        on_click: Callable = None,
        on_hover: Callable = None,
        on_hover_end: Callable = None,
    ):
        super().__init__(x, y, width, height, on_click, on_hover, on_hover_end)

        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(
            self.image, (int(width), int(height))
        )

    def draw(self, screen: pygame.Surface):
        self.blit(self.image, (0, 0))
        super().draw(screen)

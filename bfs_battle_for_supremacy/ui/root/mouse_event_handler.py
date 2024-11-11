from typing import Callable
import pygame


class MouseEventHandler:
    def __init__(
        self,
        rect: pygame.Rect,
        on_click: Callable = None,
        on_hover: Callable = None,
        on_hover_end: Callable = None,
    ):
        self.is_hovered = False
        self.is_clicked = False
        self.rect = rect
        self.on_click = on_click
        self.on_hover = on_hover
        self.on_hover_end = on_hover_end

    def merge_rects(self, rect1: pygame.Rect, rect2: pygame.Rect):
        return pygame.Rect(
            rect1.x + rect2.x,
            rect1.y + rect2.y,
            rect1.width,
            rect1.height,
        )

    def handle_mouse_event(
        self,
        event: pygame.event.Event,
        rect: pygame.Rect = pygame.Rect(0, 0, 0, 0),
    ):
        cur_rect = self.merge_rects(self.rect, rect)
        mouse_pos = pygame.mouse.get_pos()
        if cur_rect.collidepoint(mouse_pos):
            if not self.is_hovered:
                self.is_hovered = True
                self._on_hover_listener(event)
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if not self.is_clicked:
                    self.is_clicked = True
                    self._on_click_listener(event)
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                self.is_clicked = False
        else:
            if self.is_hovered:
                self._on_hover_end_listener(event)
            self.is_hovered = False

    def _on_click_listener(self, event: pygame.event.Event):
        if self.on_click:
            self.on_click(self, event)

    def _on_hover_listener(self, event: pygame.event.Event):
        if self.on_hover:
            self.on_hover(self, event)

    def _on_hover_end_listener(self, event: pygame.event.Event):
        if self.on_hover_end:
            self.on_hover_end(self, event)

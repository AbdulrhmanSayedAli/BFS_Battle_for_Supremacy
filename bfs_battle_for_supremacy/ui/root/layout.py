import pygame
from typing import Callable
from config import WIDTH, HEIGHT
from ui.root.component import Component


class Layout(Component):
    def __init__(
        self,
        on_click: Callable = None,
        on_hover: Callable = None,
        on_hover_end: Callable = None,
    ):
        super().__init__(
            0,
            0,
            WIDTH,
            HEIGHT,
            on_click,
            on_hover,
            on_hover_end,
        )

        self.components: list[Component] = []

    def draw(self, screen: pygame.Surface):
        for component in self.components:
            component.draw(self)
        super().draw(screen)

    def add_component(self, component: Component):
        self.components.append(component)

    def remove_component(self, component: Component):
        self.components.remove(component)

    def remove_component_by_index(self, index: int):
        self.components.pop(index)

    def handle_mouse_event(self, event: pygame.event.Event):
        super().handle_mouse_event(event)
        for component in self.components:
            component.handle_mouse_event(event)

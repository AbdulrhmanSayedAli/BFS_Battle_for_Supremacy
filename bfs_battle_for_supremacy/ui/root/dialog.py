from pygame.event import Event
from bfs_battle_for_supremacy.ui.root.text import Text
from bfs_battle_for_supremacy.ui.root.container import Container
from bfs_battle_for_supremacy.ui.root.rectangle import Rectangle
from bfs_battle_for_supremacy.ui.root.keyboard_event_handler import (
    KeyboardEventHandler,
)
from bfs_battle_for_supremacy.ui.utils import get_font
from .center import Center
from bfs_battle_for_supremacy.config import (
    DIALOG_HEIGHT,
    DIALOG_WIDTH,
    WIDTH,
    HEIGHT,
)
from typing import Callable
import pygame


class Dialog(Container, KeyboardEventHandler):

    def __init__(
        self,
        title_text: str,
        body_text: str,
        image_path: str = None,
        background_color=(0, 0, 0, 0),
        on_ok: Callable = None,
        on_cancel: Callable = None,
    ):
        self.on_ok = on_ok
        self.on_cancel = on_cancel
        self.image_path = image_path
        self.title = Text(
            0,
            0,
            color="black",
            secondary_color="black",
            text=title_text,
            font=get_font(50),
        )

        self.background = Rectangle(
            0,
            0,
            DIALOG_WIDTH,
            DIALOG_HEIGHT,
            background_color=background_color,
        )

        self.body = Text(
            0,
            0,
            color="black",
            secondary_color="black",
            text=body_text,
            font=get_font(30),
            width=DIALOG_WIDTH,
        )

        self.details = Text(
            0,
            DIALOG_HEIGHT - 50,
            color="black",
            secondary_color="black",
            text="press K for ok and N for cancel",
            font=get_font(30),
            width=DIALOG_WIDTH,
            height=50,
        )

        self.dialog_container = Container(
            WIDTH / 2 - DIALOG_WIDTH / 2,
            HEIGHT / 2 - DIALOG_HEIGHT / 2,
            DIALOG_WIDTH,
            DIALOG_HEIGHT,
            [
                self.background,
                Center(
                    0, 4, DIALOG_WIDTH, self.title.rect.height + 4, self.title
                ),
                Center(
                    0,
                    self.title.rect.height + 8,
                    DIALOG_WIDTH,
                    DIALOG_HEIGHT - (self.title.rect.height + 8) - 50,
                    self.body,
                ),
                self.details,
            ],
        )
        from bfs_battle_for_supremacy.ui.root import Image

        container_components = [
            Rectangle(0, 0, WIDTH, HEIGHT, background_color=(0, 0, 0, 150)),
            self.dialog_container,
        ]

        if self.image_path:
            container_components.append(
                Center(
                    0,
                    0,
                    WIDTH,
                    200,
                    Image(
                        0,
                        0,
                        200,
                        200,
                        self.image_path,
                    ),
                ),
            )

        Container.__init__(
            self,
            0,
            0,
            WIDTH,
            HEIGHT,
            container_components,
        )

        self._title_text = title_text
        self._body_text = body_text
        self._background_color = background_color

    @property
    def title_text(self):
        return self._title_text

    @title_text.setter
    def title_text(self, value):
        self._title_text = value
        self.title.text = value

    @property
    def body_text(self):
        return self._body_text

    @body_text.setter
    def body_text(self, value):
        self._body_text = value
        self.body.text = value

    @property
    def background_color(self):
        return self._background_color

    @background_color.setter
    def background_color(self, value):
        self._background_color = value
        self.background.background_color = value

    def handle_keyboard_event(self, event: Event):
        if event.key == pygame.K_k:
            self.on_ok()
        elif event.key == pygame.K_n:
            self.on_cancel()
        super().handle_keyboard_event(event)

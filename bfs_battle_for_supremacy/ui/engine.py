from bfs_battle_for_supremacy.ui.root import Layout
import pygame
from bfs_battle_for_supremacy.config import (
    WIDTH,
    HEIGHT,
    FRAME_RATE_PER_SECOND,
    IMAGES_PATH,
)
import sys
import os


class Engine:
    # Static class variables
    screen = None
    running = True
    clock = None
    layouts = []
    current_layout = 0

    @staticmethod
    def init(
        layouts: list[Layout] = [], caption="Cards", current_layout: int = 0
    ):
        Engine.init_pygame(caption)
        Engine.running = True
        Engine.layouts = layouts
        Engine.current_layout = current_layout

    @staticmethod
    def init_pygame(caption):
        pygame.init()
        Engine.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(caption)
        icon_image = pygame.image.load(os.path.join(IMAGES_PATH, "icon.webp"))
        pygame.display.set_icon(icon_image)
        Engine.clock = pygame.time.Clock()

    @staticmethod
    def layout() -> Layout:
        return Engine.layouts[Engine.current_layout]

    @staticmethod
    def navigate(index: int):
        Engine.current_layout = index

    @staticmethod
    def start():
        while Engine.running:
            Engine.layout().fill("grey")
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type in [
                    pygame.MOUSEBUTTONDOWN,
                    pygame.MOUSEMOTION,
                    pygame.MOUSEBUTTONUP,
                ]:
                    Engine.layout().handle_mouse_event(event)

                if event.type == pygame.KEYDOWN:
                    Engine.layout().handle_keyboard_event(event)
            Engine.layout().draw(Engine.screen)

            pygame.display.flip()
            Engine.clock.tick(FRAME_RATE_PER_SECOND)

    @staticmethod
    def quit():
        Engine.running = False

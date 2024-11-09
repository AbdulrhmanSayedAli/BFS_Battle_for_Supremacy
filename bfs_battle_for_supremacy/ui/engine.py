from ui.root.layout import Layout
import pygame
from config import WIDTH, HEIGHT, FRAME_RATE_PER_SECOND
import sys


class Engine:
    def __init__(
        self,
        layouts: list[Layout] = [],
        caption="Cards",
        current_layout: int = 0,
    ):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(caption)
        self.running = True
        self.clock = pygame.time.Clock()

        self.layouts = layouts
        self.current_layout = current_layout

    @property
    def layout(self) -> Layout:
        return self.layouts[self.current_layout]

    def start(self):
        while self.running:
            self.layout.fill("grey")
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type in [
                    pygame.MOUSEBUTTONDOWN,
                    pygame.MOUSEMOTION,
                    pygame.MOUSEBUTTONUP,
                ]:
                    self.layout.handle_mouse_event(event)

                if event.type == pygame.KEYDOWN:
                    pass
            self.layout.draw(self.screen)

            pygame.display.flip()
            self.clock.tick(FRAME_RATE_PER_SECOND)

from ui.root.component import Component
from ui.root.button import Button
from ui.root.layout import Layout
from ui.engine import Engine
import pygame

engine = Engine()
font = pygame.font.Font(None, 26)


c = Button(
    10,
    10,
    200,
    100,
    color="red",
    secondary_color="blue",
    text="click me here",
    font=font,
)


def d(c: Component, event):
    c.x += 10
    c.y += 10


c.on_click = d


layout = Layout()
layout.add_component(c)
layout.fill("grey")


engine.layouts = [layout]

engine.start()

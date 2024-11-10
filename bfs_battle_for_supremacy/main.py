from ui.root.component import Component
from ui.root.button import Button
from ui.root.text import Text
from ui.root.layout import Layout
from ui.engine import Engine
import pygame

engine = Engine()
font = pygame.font.Font(None, 56)


button = Button(
    10,
    10,
    200,
    100,
    color="red",
    secondary_color="blue",
    text="click me here",
    font=font,
)

text = Text(500, 100, "red", "blue", "Hi this is a text", font)


def d(c: Component, event):
    c.x += 10
    c.y += 10


button.on_click = d


layout = Layout()
layout.add_component(button)
layout.add_component(text)
layout.fill("grey")


engine.layouts = [layout]

engine.start()

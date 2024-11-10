from ui.root.component import Component
from ui.root.button import Button
from ui.root.text import Text
from ui.root.layout import Layout
from ui.root.image import Image
from ui.engine import Engine
from config import WIDTH, HEIGHT, IMAGES_PATH
import pygame

Engine.init()
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


image = Image(0, 0, WIDTH, HEIGHT, IMAGES_PATH + "main_menu_background.webp")

layout = Layout()
layout.add_component(image)
layout.add_component(button)
layout.add_component(text)
layout.fill("grey")


Engine.layouts = [layout]
Engine.start()

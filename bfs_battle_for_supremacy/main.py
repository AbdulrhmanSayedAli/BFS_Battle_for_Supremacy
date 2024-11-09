from ui.root.component import Component
from ui.root.layout import Layout
from ui.engine import Engine


c = Component(10, 10, 100, 100)
c.fill("red")


def d(c: Component, event):
    c.x += 10
    c.y += 10


c.on_click = d


layout = Layout()
layout.add_component(c)
layout.fill("grey")


engine = Engine(layouts=[layout])

engine.start()

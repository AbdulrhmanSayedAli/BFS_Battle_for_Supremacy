from ui.engine import Engine
from ui.layouts.main_menu import MainMenu

Engine.init()


layout = MainMenu()


Engine.layouts = [layout]
Engine.start()

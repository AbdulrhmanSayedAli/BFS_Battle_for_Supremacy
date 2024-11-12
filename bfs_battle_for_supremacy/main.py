from ui.engine import Engine
from ui.layouts.main_menu import MainMenu
from ui.layouts.game import Game

Engine.init()


Engine.layouts = [MainMenu(), Game()]
Engine.start()

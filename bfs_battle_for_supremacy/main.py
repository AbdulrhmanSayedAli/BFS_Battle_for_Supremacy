from bfs_battle_for_supremacy.ui.engine import Engine
from bfs_battle_for_supremacy.ui.layouts.game_over import GameOver
from bfs_battle_for_supremacy.ui.layouts.main_menu import MainMenu
from bfs_battle_for_supremacy.ui.layouts.game import Game

Engine.init()


Engine.layouts = [MainMenu(), Game(),GameOver()]
Engine.start()

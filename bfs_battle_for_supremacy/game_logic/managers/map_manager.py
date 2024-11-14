from bfs_battle_for_supremacy.game_logic.entities.map import Map
from bfs_battle_for_supremacy.game_logic.entities.square import Square

class MapManager:
    game_map = Map(10, 10)  

    @staticmethod
    def check_availability(square: Square):
        return square.is_empty

    @staticmethod
    def place_item(square: Square, item):
        if square.is_empty:
            square.set_content(item)
            return True
        return False

    @staticmethod
    def remove_item(square: Square):
        square.clear_content()

    @staticmethod
    def move_item(current_square: Square, target_square: Square):
        if MapManager.check_availability(target_square):
            item = current_square.get_content()
            MapManager.remove_item(current_square)
            MapManager.place_item(target_square, item)
            return True
        return False
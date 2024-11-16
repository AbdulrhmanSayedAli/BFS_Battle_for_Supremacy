from bfs_battle_for_supremacy.game_logic.entities.map import Map
from bfs_battle_for_supremacy.game_logic.entities.square import Square
from collections import deque


class MapManager:
    game_map = Map(10, 10)
    movement_counter = 20

    current_position = None
    current_object = None
    target_position = None
    selection_counter = 0

    @staticmethod
    def reset_movement_counter():
        MapManager.movement_counter = 20

    @staticmethod
    def reset_selection():
        MapManager.current_position = None
        MapManager.current_object = None
        MapManager.target_position = None
        MapManager.selection_counter = 0

    @staticmethod
    def select_square(square: Square, current_player):

        if MapManager.selection_counter == 0:
            if (
                not square.is_empty
                and square.get_content()
                in [current_player] + current_player.monsters
            ):
                MapManager.current_position = square
                MapManager.current_object = square.get_content()
                MapManager.selection_counter = 1
                print(
                    "Selected current position: "
                    + f"({square.row},{square.column})"
                )
            else:
                print("Invalid selection. Please select a valid object.")
        elif MapManager.selection_counter == 1:
            if MapManager.check_availability(square):
                MapManager.target_position = square
                MapManager.selection_counter = 2
                print(
                    "Selected target position:"
                    + f"({square.row}, {square.column})"
                )
                MapManager.move_with_bfs(current_player)
            else:
                print(
                    "Target position is not empty."
                    + "Please select an empty square."
                )
        else:
            print("Too many selections. Resetting selection.")
            MapManager.reset_selection()

    @staticmethod
    def bfs_path_finding(start_square, target_square):
        rows = len(MapManager.game_map.grid)
        cols = len(MapManager.game_map.grid[0])

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visited = set()
        queue = deque([(start_square, [])])

        while queue:
            current_square, path = queue.popleft()

            if current_square == target_square:
                return path + [target_square]

            if current_square in visited:
                continue

            visited.add(current_square)

            for direction in directions:
                next_row = current_square.row + direction[0]
                next_col = current_square.column + direction[1]

                if 0 <= next_row < rows and 0 <= next_col < cols:
                    next_square = MapManager.game_map.get_square(
                        next_row, next_col
                    )
                    if (
                        MapManager.check_availability(next_square)
                        and next_square not in visited
                    ):
                        queue.append((next_square, path + [current_square]))

        return []

    @staticmethod
    def move_with_bfs(current_player):

        if not MapManager.current_position or not MapManager.target_position:
            print("Positions not set. Cannot move object.")
            return

        path = MapManager.bfs_path_finding(
            MapManager.current_position, MapManager.target_position
        )

        if not path:
            print("No valid path found.")
            MapManager.reset_selection()
            return

        distance = len(path) - 1
        if distance > MapManager.movement_counter:
            print(
                "Move exceeds remaining movement points "
                + f"({MapManager.movement_counter})."
            )
            MapManager.reset_selection()
            return

        item = MapManager.current_object
        for step in path[1:]:
            MapManager.remove_item(MapManager.current_position)
            MapManager.place_item(step, item)
            MapManager.current_position = step

        MapManager.movement_counter -= distance
        print(f"Moved {item} along path: {path}")
        print(f"Remaining movement points: {MapManager.movement_counter}")

        MapManager.reset_selection()

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

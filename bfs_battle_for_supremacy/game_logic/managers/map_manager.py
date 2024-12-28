import os
from config import *
from bfs_battle_for_supremacy.game_logic.entities.map import Map
from bfs_battle_for_supremacy.game_logic.entities.square import Square
from bfs_battle_for_supremacy.game_logic.entities.card import Card
from bfs_battle_for_supremacy.game_logic.entities.player import Player
from bfs_battle_for_supremacy.game_logic.entities.rock import Rock
import random
from collections import deque
import asyncio


class MapManager:
    game_map = Map(10, 10)
    movement_counter = 20

    current_position = None
    current_object = None
    target_position = None
    selection_counter = 0
    limit_attack_counter = 2
    attack_counter = {}

    @staticmethod
    def initialize_map(player1: Player, player2: Player):

        player1_square = MapManager.game_map.get_square(0, 0)
        if player1_square:
            MapManager.place_item(player1_square, player1)
            player1.position = player1_square

        rows = len(MapManager.game_map.grid)
        cols = len(MapManager.game_map.grid[0])
        player2_square = MapManager.game_map.get_square(rows - 1, cols - 1)
        if player2_square:
            MapManager.place_item(player2_square, player2)
            player2.position = player2_square

        rock_image_path = os.path.join(IMAGES_PATH, "rock.png")
        for _ in range(ROCK_NUM):
            while True:
                random_row = random.randint(0, rows - 1)
                random_col = random.randint(0, cols - 1)
                random_square = MapManager.game_map.get_square(
                    random_row, random_col
                )
                if random_square and random_square.is_empty:
                    rock = Rock(image_path=rock_image_path)
                    MapManager.place_item(random_square, rock)
                    break

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
    async def select_square(square: Square, current_player):
        if MapManager.selection_counter == 0:
            if not square.is_empty:
                content = square.get_content()
                if content == current_player or (
                    isinstance(content, Card)
                    and content.type in ["monster", "building"]
                    and content in current_player.cards
                ):
                    MapManager.current_position = square
                    MapManager.current_object = content
                    MapManager.selection_counter = 1
                    print( f"Selected object: {content}.")
                else:
                    print( "Invalid selection. Please select a valid object.")
            else:
                return print("Invalid selection. Square is empty.")

        elif MapManager.selection_counter == 1:
            content = square.get_content()
            print("contene",content)
            print("current_player",current_player)
            if content == current_player or (
                isinstance(content, Card) and content in current_player.cards
            ):
                MapManager.current_position = square
                MapManager.current_object = content
                print( f"Re-selected object: {content}.")

            if content and ((
                isinstance(content, Card)
                and content not in current_player.cards
            ) or content != current_player):
                current_attacker = MapManager.current_object
                attack_count = MapManager.attack_counter.get(
                    current_attacker, 0
                )

                if attack_count >= MapManager.limit_attack_counter:
                    print (
                        f"{current_attacker} has already attacked "
                        + f"{MapManager.limit_attack_counter}"
                        + " this turn. Cannot attack again."
                    )

                nearest_squares = (
                    MapManager.find_nearest_empty_squares_limited(square)
                )
                if nearest_squares:
                    for nearest_square in nearest_squares:
                        MapManager.target_position = nearest_square
                        success = await MapManager.move_with_bfs()
                        if success:
                            MapManager.attack_counter[current_attacker] = (
                                MapManager.attack_counter.get(
                                    current_attacker, 0
                                )
                                + 1
                            )
                            print( f"Attacked {content} successfully.")
                    print (
                        "No valid path to any nearby square. "
                        + "Attack failed."
                    )
                else:
                    print (
                        "No empty squares near the target. "
                        + "Attack not possible."
                    )

            elif MapManager.check_availability(square):
                MapManager.target_position = square
                MapManager.selection_counter = 2
                await MapManager.move_with_bfs()
                print( 
                    "Moved to target position: "
                    + f"({square.row}, {square.column})."
                )
            else:
                print( 
                    "Target position is not empty. "
                    + "Please select an empty square."
                )

        else:
            print( "Ignoring extra selection during movement.")

    @staticmethod
    def find_nearest_empty_squares_limited(target_square: Square):
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        empty_squares = []

        for direction in directions:
            new_row = target_square.row + direction[0]
            new_col = target_square.column + direction[1]
            if MapManager.is_within_bounds(new_row, new_col):
                adjacent_square = MapManager.game_map.get_square(
                    new_row, new_col
                )
                if adjacent_square.is_empty:
                    empty_squares.append(adjacent_square)

        return empty_squares

    @staticmethod
    async def move_with_bfs(delay=0.5, attack_target=None):
        if not MapManager.current_position or not MapManager.target_position:
            print("Positions not set. Cannot move object.")
            return False
        
        path:list[Square] = MapManager.bfs_path_finding(
            MapManager.current_position, MapManager.target_position
        )
        print("current_position",MapManager.current_position)
        print("target_position",MapManager.target_position)
        print(path)
        if not path:
            print(
                "No valid path to target position"
                + f" ({MapManager.target_position.row},"
                + f" {MapManager.target_position.column})."
            )
            return False

        distance = len(path) - 1

        if distance > MapManager.movement_counter:
            print(
                "Move exceeds remaining movement points "
                + f"({MapManager.movement_counter})."
            )
            return False

        item = MapManager.current_object
        for step in path[1:]:
            MapManager.remove_item(MapManager.current_position)
            MapManager.place_item(step, item)
            if isinstance(item, Card):
                item.location = step
            elif isinstance(item, Player):
                item.position = step
            MapManager.current_position = step
            print(f"Moved {item} to ({step.row}, {step.column})")
            await asyncio.sleep(delay)

        if attack_target:
            print(f"Attacking {attack_target.title} with {item}.")
            attack_target.health -= item.damage
            print(
                f"{attack_target.title} took {item.damage} damage. "
                + f"Remaining health: {attack_target.health}"
            )
            if attack_target.health <= 0:
                print(f"{attack_target.title} has been destroyed.")
                MapManager.remove_item(MapManager.target_position)

        MapManager.movement_counter -= distance
        print(f"Remaining movement points: {MapManager.movement_counter}")
        MapManager.reset_selection()
        return True

    @staticmethod
    def bfs_path_finding(start_square, target_square):
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
                new_row = current_square.row + direction[0]
                new_col = current_square.column + direction[1]

                if MapManager.is_within_bounds(new_row, new_col):
                    next_square = MapManager.game_map.get_square(
                        new_row, new_col
                    )
                    if (
                        MapManager.check_availability(next_square)
                        and next_square not in visited
                    ):
                        queue.append((next_square, path + [current_square]))

        return []

    @staticmethod
    def is_within_bounds(row, col):
        return 0 <= row < len(MapManager.game_map.grid) and 0 <= col < len(
            MapManager.game_map.grid[0]
        )

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
    def reset_attack_counter():
        MapManager.attack_counter = {}

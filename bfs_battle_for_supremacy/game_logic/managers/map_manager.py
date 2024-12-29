import os
from bfs_battle_for_supremacy.game_logic.entities.map import Map
from bfs_battle_for_supremacy.game_logic.entities.square import Square
from bfs_battle_for_supremacy.game_logic.entities.card import Card
from bfs_battle_for_supremacy.game_logic.entities.player import Player
from bfs_battle_for_supremacy.game_logic.entities.rock import Rock
import random
from collections import deque
import asyncio
from bfs_battle_for_supremacy.config import IMAGES_PATH, ROCK_NUM


class MapManager:
    game_map = Map(10, 10)
    movement_counter = 20

    current_position = None
    current_object = None
    target_position = None
    selection_counter = 0
    limit_attack_counter = 2
    attack_counter = {}
    is_moving = False

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
        print("Selection resetted")
        return True

    @staticmethod
    def set_selection(square, content):
        if square == MapManager.current_position:
            return MapManager.reset_selection()
        MapManager.current_position = square
        MapManager.current_object = content
        MapManager.selection_counter = 1
        print(f"Selected object: {content}.")
        return True

    @staticmethod
    async def select_square(square: Square, current_player):
        content = square.get_content()
        if MapManager.selection_counter == 0:
            if not square.is_empty:
                if content == current_player or (
                    isinstance(content, Card)
                    and content in current_player.cards
                ):
                    return MapManager.set_selection(square, content)
                else:
                    print("Invalid selection. Please select a valid object.")
                    return
            else:
                return MapManager.reset_selection()

        elif MapManager.selection_counter == 1:
            if content == current_player or (
                isinstance(content, Card) and content in current_player.cards
            ):
                return MapManager.set_selection(square, content)

            if (
                not isinstance(MapManager.current_object, Player)
                and MapManager.current_object.type == "building"
            ):
                return MapManager.reset_selection()
            if content and (
                (
                    isinstance(content, Card)
                    and content not in current_player.cards
                )
                or content != current_player
            ):
                current_attacker = MapManager.current_object
                MapManager.target_position = square
                attack_count = MapManager.attack_counter.get(
                    current_attacker, 0
                )

                if attack_count >= MapManager.limit_attack_counter:
                    print(
                        f"{current_attacker} has already attacked "
                        + f"{MapManager.limit_attack_counter} times this turn."
                        + "Cannot attack again."
                    )
                    return

                path = MapManager.bfs_path_finding(
                    MapManager.current_position,
                    MapManager.target_position,
                    allow_enemy=True,
                )
                if path:

                    attack_position = MapManager.target_position
                    path.pop()
                    MapManager.target_position = path[-1]
                    await MapManager.move_with_bfs(
                        attack_position=attack_position
                    )
                    MapManager.attack_counter[current_attacker] = (
                        MapManager.attack_counter.get(current_attacker, 0) + 1
                    )
                    print(f"Attacked {content} successfully.")
                    return
                print(
                    "No valid path to any nearby square. " + "Attack failed."
                )
                return

            elif MapManager.check_availability(square, allow_enemy=False):
                MapManager.target_position = square
                MapManager.selection_counter = 2
                await MapManager.move_with_bfs()
                print(
                    "Moved to target position: "
                    + f"({square.row}, {square.column})."
                )
                return
            else:
                print(
                    "Target position is not empty. "
                    + "Please select an empty square."
                )
                return

        else:
            if not MapManager.is_moving:
                return MapManager.reset_selection()

            print("Ignoring extra selection during movement.")

    @staticmethod
    async def move_with_bfs(delay=0.5, attack_position=None):
        if MapManager.is_moving:
            print("Movement is already in progress. Please wait.")
            return False

        MapManager.is_moving = True

        print(f"CUR-POS : {MapManager.current_position}")
        print(f"TAR-POS {MapManager.target_position}")

        if not MapManager.current_position or not MapManager.target_position:
            print("Positions not set. Cannot move object.")
            MapManager.is_moving = False
            return False

        path: list[Square] = MapManager.bfs_path_finding(
            MapManager.current_position, MapManager.target_position
        )

        if not path:
            print(
                "No valid path to target position"
                + f" ({MapManager.target_position.row},"
                + f" {MapManager.target_position.column})."
            )
            MapManager.is_moving = False
            return False

        item = MapManager.current_object

        target_content = MapManager.target_position.get_content()

        if isinstance(target_content, Rock):
            print("Cannot move to a square containing a rock.")
            MapManager.is_moving = False
            return False

        if target_content and target_content != item:
            if len(path) > 1:
                path = path[:-1]

        distance = len(path) - 1

        if distance > MapManager.movement_counter:
            print(
                "Move exceeds remaining movement points "
                + f"({MapManager.movement_counter})."
            )
            MapManager.is_moving = False
            return False

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

        if attack_position:
            attack_target = attack_position.get_content()
            try:
                attack_target_name = attack_target.name
            except:
                attack_target_name = attack_target.title

            print(f"Attacking {attack_target_name} with {item}.")
            attack_target.health -= item.damage
            print(
                f"{attack_target_name} took {item.damage} damage. "
                + f"Remaining health: {attack_target.health}"
            )
            if attack_target.health <= 0:
                print(f"{attack_target_name} has been destroyed.")
                from bfs_battle_for_supremacy.game_logic.managers.player_manager import (
                    PlayerManager,
                )
                
                if isinstance(attack_target,Player):
                    attack_target.has_lost = True
                    print(attack_target.has_lost)
                    print(PlayerManager.players[0].has_lost)
                    print(PlayerManager.players[1].has_lost)
                    return

                PlayerManager.remove_card(
                    (PlayerManager.current_player_index + 1) % 2,
                    attack_position,
                )

        MapManager.movement_counter -= distance
        print(f"Remaining movement points: {MapManager.movement_counter}")
        MapManager.reset_selection()

        MapManager.is_moving = False
        return True

    @staticmethod
    def bfs_path_finding(start_square, target_square, allow_enemy=False):
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
                    # next_content = next_square.get_content()

                    if next_square == target_square or (
                        MapManager.check_availability(
                            next_square, allow_enemy=allow_enemy
                        )
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
    def check_availability(square, allow_enemy=False):
        if square.is_empty:
            return True
        if allow_enemy and isinstance(square.get_content(), Card):
            return True
        if allow_enemy and isinstance(square.get_content(), Player):
            return True
        return False

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

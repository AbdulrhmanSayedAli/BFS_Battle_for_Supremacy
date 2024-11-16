import unittest
from bfs_battle_for_supremacy.game_logic.managers.player_manager import (
    PlayerManager,
)
from bfs_battle_for_supremacy.game_logic.managers.map_manager import MapManager
from bfs_battle_for_supremacy.game_logic.entities.player import Player
from bfs_battle_for_supremacy.game_logic.entities.resources import Resources
from bfs_battle_for_supremacy.game_logic.entities.monster import Monster
from bfs_battle_for_supremacy.game_logic.entities.building import Building
from bfs_battle_for_supremacy.game_logic.entities.map import Map


class TestGameLogic(unittest.TestCase):
    def setUp(self):
        self.player1 = Player("Player 1")
        self.player2 = Player("Player 2")
        PlayerManager.players = [self.player1, self.player2]
        PlayerManager.current_player_index = 0
        MapManager.reset_movement_counter()
        MapManager.reset_selection()

    def test_request_card(self):
        card_data = {
            "title": "Dragon",
            "description": "A powerful dragon",
            "ability": "Fire Breath",
            "type": "monster",
            "valid_for": -1,
            "rarity": "epic",
            "number_of_uses": 1,
            "yields": {
                "each_turn": {"food": 1, "wood": 2, "iron": 0, "coins": 3}
            },
            "consumes": {
                "instant": {"food": 5, "wood": 5, "iron": 0, "coins": 5}
            },
            "stats": {"health": 50, "damage": 15},
        }

        self.player1.resources = Resources(food=10, wood=10, iron=5, coins=10)

        player_card = Monster(**card_data)
        self.player1.add_card(player_card)
        self.assertIn(player_card, self.player1.cards)

    def test_process_recurring_costs(self):
        card_data = {
            "title": "Farm",
            "description": "Produces food",
            "ability": "Harvest",
            "type": "building",
            "valid_for": 3,
            "rarity": "common",
            "number_of_uses": 1,
            "yields": {
                "each_turn": {"food": 2, "wood": 0, "iron": 0, "coins": 0}
            },
            "consumes": {
                "each_turn": {"food": 0, "wood": 1, "iron": 0, "coins": 0}
            },
        }

        building = Building(**card_data)
        self.player1.add_card(building)
        self.player1.resources = Resources(food=4, wood=5, iron=0, coins=0)
        initial_food = self.player1.resources.food
        initial_wood = self.player1.resources.wood

        PlayerManager.process_recurring_costs()

        self.assertEqual(self.player1.resources.food, initial_food + 2)
        self.assertEqual(self.player1.resources.wood, initial_wood - 1)

    def test_bfs_pathfinding_and_movement(self):
        MapManager.game_map = Map(10, 10)
        square1 = MapManager.game_map.get_square(0, 0)
        square2 = MapManager.game_map.get_square(3, 3)
        monster = Monster(
            title="Dragon",
            description="A powerful dragon",
            ability="Fire Breath",
            stats={"health": 50, "damage": 15},
            valid_for=-1,
            rarity="epic",
            number_of_uses=1,
            yields={
                "each_turn": {"food": 1, "wood": 2, "iron": 0, "coins": 3}
            },
            consumes={
                "instant": {"food": 5, "wood": 5, "iron": 0, "coins": 5}
            },
        )

        MapManager.place_item(square1, monster)
        self.player1.monsters.append(monster)

        MapManager.select_square(square1, self.player1)
        MapManager.select_square(square2, self.player1)

        self.assertEqual(MapManager.movement_counter, 14)
        self.assertTrue(square2.get_content() is monster)
        self.assertTrue(square1.is_empty)

    def test_selection_reset(self):
        MapManager.game_map = Map(10, 10)
        square1 = MapManager.game_map.get_square(0, 0)
        square3 = MapManager.game_map.get_square(5, 5)
        square4 = MapManager.game_map.get_square(6, 6)

        monster = Monster(
            title="Dragon",
            description="Fierce Dragon",
            ability="Fire Breath",
            stats={"health": 50, "damage": 20},
            valid_for=-1,
            rarity="epic",
            number_of_uses=1,
            yields={
                "each_turn": {"food": 1, "wood": 2, "iron": 0, "coins": 3}
            },
            consumes={
                "instant": {"food": 5, "wood": 5, "iron": 0, "coins": 5}
            },
        )
        MapManager.place_item(square1, monster)
        self.player1.monsters.append(monster)

        self.player1.position = square3
        MapManager.place_item(square3, self.player2)

        MapManager.select_square(square1, self.player1)
        self.assertEqual(MapManager.selection_counter, 1)

        MapManager.select_square(square3, self.player1)
        self.assertEqual(MapManager.selection_counter, 1)

        MapManager.select_square(square4, self.player1)
        self.assertEqual(MapManager.selection_counter, 0)

    def test_toggle_turn(self):
        PlayerManager.toggle_turn()
        self.assertEqual(PlayerManager.current_player_index, 1)
        self.assertEqual(MapManager.movement_counter, 20)
        self.assertEqual(MapManager.selection_counter, 0)


if __name__ == "__main__":
    unittest.main()

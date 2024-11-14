import unittest
from bfs_battle_for_supremacy.game_logic.managers.player_manager import PlayerManager
from bfs_battle_for_supremacy.game_logic.managers.cards_manager import CardsManager
from bfs_battle_for_supremacy.game_logic.managers.map_manager import MapManager
from bfs_battle_for_supremacy.game_logic.managers.resources_manager import ResourcesManager
from bfs_battle_for_supremacy.game_logic.entities.player import Player
from bfs_battle_for_supremacy.game_logic.entities.resources import Resources
from bfs_battle_for_supremacy.game_logic.entities.square import Square
from bfs_battle_for_supremacy.game_logic.entities.card import Card
from bfs_battle_for_supremacy.game_logic.entities.monster import Monster
from bfs_battle_for_supremacy.game_logic.entities.building import Building

class TestGameLogic(unittest.TestCase):

    def setUp(self):
        self.player1 = Player("Player 1")
        self.player2 = Player("Player 2")
        PlayerManager.players = [self.player1, self.player2]
        PlayerManager.current_player_index = 0

    def test_request_card(self):
        card_data = {
            "title": "Dragon",
            "description": "A powerful dragon",
            "ability": "Fire Breath",
            "type": "monster",
            "valid_for": -1,
            "rarity": "epic",
            "number_of_uses": 1,
            "yields": {"each_turn": {"food": 1, "wood": 2, "iron": 0, "coins": 3}},
            "consumes": {"instant": {"food": 5, "wood": 5, "iron": 0, "coins": 5}},
            "stats": {"health": 50, "damage": 15}
        }

        self.player1.resources = Resources(food=10, wood=10, iron=5, coins=10)
        
        CardsManager.current_card = Monster(**card_data)
        player_card = PlayerManager.request_card()
        self.assertIsNotNone(player_card)
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
            "yields": {"each_turn": {"food": 2, "wood": 0, "iron": 0, "coins": 0}},
            "consumes": {"each_turn": {"food": 0, "wood": 1, "iron": 0, "coins": 0}}
        }

        building = Building(**card_data)
        self.player1.add_card(building)
        
        self.player1.resources = Resources(food=4, wood=5, iron=0, coins=0)
        initial_food = self.player1.resources.food
        initial_wood = self.player1.resources.wood
        
        PlayerManager.process_recurring_costs()
        
        self.assertEqual(self.player1.resources.food, initial_food + 2)  
        self.assertEqual(self.player1.resources.wood, initial_wood - 1)  

    def test_map_manager(self):
        square1 = Square(0, 0)
        square2 = Square(1, 1)
        
        monster_data = {
            "title": "Dragon",
            "description": "Fierce Dragon",
            "ability": "Flame Attack",
            "stats": {"health": 50, "damage": 20},
            "valid_for": -1,
            "rarity": "epic",
            "number_of_uses": 1,
            "yields": {"each_turn": {"food": 1, "wood": 2, "iron": 0, "coins": 3}},
            "consumes": {"instant": {"food": 5, "wood": 5, "iron": 0, "coins": 5}}
        }
        
        monster = Monster(**monster_data)

        self.assertTrue(MapManager.check_availability(square1))
        MapManager.place_item(square1, monster)
        self.assertFalse(MapManager.check_availability(square1))

        self.assertTrue(MapManager.move_item(square1, square2))
        self.assertTrue(MapManager.check_availability(square1))
        self.assertFalse(MapManager.check_availability(square2))

if __name__ == '__main__':
    unittest.main()

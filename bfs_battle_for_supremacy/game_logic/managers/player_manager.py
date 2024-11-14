from bfs_battle_for_supremacy.game_logic.entities.player import Player
from bfs_battle_for_supremacy.game_logic.managers.cards_manager import (
    CardsManager,
)
from bfs_battle_for_supremacy.game_logic.managers.map_manager import MapManager


class PlayerManager:
    players = [Player("Player 1"), Player("Player 2")]
    current_player_index = 0

    @staticmethod
    def toggle_turn():
        PlayerManager.current_player_index = (
            1 - PlayerManager.current_player_index
        )

    @staticmethod
    def request_card():
        current_player = PlayerManager.players[
            PlayerManager.current_player_index
        ]
        enemy_player = PlayerManager.players[
            1 - PlayerManager.current_player_index
        ]

        card = CardsManager.provide_card(current_player)
        if card and CardsManager.activate_card(
            card, current_player, enemy_player
        ):
            return card
        return None

    @staticmethod
    def process_recurring_costs():
        current_player = PlayerManager.players[
            PlayerManager.current_player_index
        ]
        enemy_player = PlayerManager.players[
            1 - PlayerManager.current_player_index
        ]
        CardsManager.process_recurring_effects(current_player, enemy_player)

    @staticmethod
    def place_card_on_map(card, target_square):
        if MapManager.check_availability(target_square):
            MapManager.place_item(target_square, card)
            return True
        return False

    @staticmethod
    def move_player_to_square(player, target_square):
        current_square = player.position
        if MapManager.move_item(current_square, target_square):
            player.position = target_square
            return True
        return False

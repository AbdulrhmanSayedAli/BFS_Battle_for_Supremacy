from bfs_battle_for_supremacy.game_logic.entities.player import Player
from bfs_battle_for_supremacy.game_logic.managers.cards_manager import (
    CardsManager,
)
from bfs_battle_for_supremacy.game_logic.managers.map_manager import MapManager
from bfs_battle_for_supremacy.game_logic.entities.square import Square


class PlayerManager:
    players = [Player("Player 1"), Player("Player 2")]
    current_player_index = 0

    @staticmethod
    def toggle_turn():
        PlayerManager.current_player_index = (
            1 - PlayerManager.current_player_index
        )
        MapManager.reset_movement_counter()
        MapManager.reset_selection()

    @staticmethod
    def request_card():
        current_player = PlayerManager.players[
            PlayerManager.current_player_index
        ]
        card = CardsManager.provide_card(current_player)
        return card

    @staticmethod
    def activate_card(card):
        current_player = PlayerManager.players[
            PlayerManager.current_player_index
        ]
        enemy_player = PlayerManager.players[
            1 - PlayerManager.current_player_index
        ]

        if card and CardsManager.activate_card(
            card, current_player, enemy_player
        ):
            return True
        return False

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
    def select_square_for_current_player(square: Square):
        current_player = PlayerManager.players[
            PlayerManager.current_player_index
        ]
        MapManager.select_square(square, current_player)

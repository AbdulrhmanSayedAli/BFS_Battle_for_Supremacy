from bfs_battle_for_supremacy.game_logic.entities.player import Player
from bfs_battle_for_supremacy.game_logic.managers.cards_manager import (
    CardsManager,
)
from bfs_battle_for_supremacy.game_logic.managers.map_manager import MapManager
from bfs_battle_for_supremacy.game_logic.entities.square import Square
import asyncio


class PlayerManager:
    players = [Player("Player 1"), Player("Player 2")]
    current_player_index = 0
    card_drawn_this_turn = [False, False]

    @staticmethod
    def toggle_turn():
        if MapManager.is_moving:
            return
        PlayerManager.card_drawn_this_turn[
            PlayerManager.current_player_index
        ] = False
        PlayerManager.current_player_index = (
            1 - PlayerManager.current_player_index
        )
        MapManager.reset_movement_counter()
        MapManager.reset_selection()
        MapManager.reset_attack_counter()
        PlayerManager.process_recurring_costs()

    @staticmethod
    def request_card():
        current_player = PlayerManager.players[
            PlayerManager.current_player_index
        ]

        if PlayerManager.card_drawn_this_turn[
            PlayerManager.current_player_index
        ]:
            print(f"{current_player.name} has already drawn a card this turn.")
            return None

        card = CardsManager.provide_card()
        if card:
            PlayerManager.card_drawn_this_turn[
                PlayerManager.current_player_index
            ] = True
        return card

    @staticmethod
    def activate_card(card, target_square: Square):
        current_player = PlayerManager.players[
            PlayerManager.current_player_index
        ]
        enemy_player = PlayerManager.players[
            1 - PlayerManager.current_player_index
        ]

        if card and CardsManager.activate_card(
            card, current_player, enemy_player, target_square
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
        results = CardsManager.process_recurring_effects(
            current_player, enemy_player
        )
        return results

    @staticmethod
    def select_square_for_current_player(square: Square):
        current_player = PlayerManager.players[
            PlayerManager.current_player_index
        ]
        asyncio.run(MapManager.select_square(square, current_player))

    @staticmethod
    def remove_card(player, square):
        if isinstance(player, int):
            player = PlayerManager.players[player]
        card = square.get_content()
        if card not in player.cards:
            print("card not found.")
            return False
        player.cards.remove(card)
        MapManager.remove_item(square)
        print(f"card {card.title} removed.")

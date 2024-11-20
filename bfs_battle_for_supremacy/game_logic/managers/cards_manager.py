from bfs_battle_for_supremacy.game_logic.entities.card import Card
from bfs_battle_for_supremacy.game_logic.utilities.ai_handler import (
    OpenAIHandler,
)
from bfs_battle_for_supremacy.game_logic.managers.resources_manager import (
    ResourcesManager,
)


class CardsManager:
    loading = False
    finished = False
    current_card = None
    negative_resources_count = {}

    @staticmethod
    def provide_card(player):
        CardsManager.loading = True
        card_data = OpenAIHandler.send_card_request()

        card_type = card_data.get("type")
        if not card_type:
            CardsManager.loading = False
            return None

        card = Card(**card_data)

        CardsManager.current_card = card
        CardsManager.loading = False
        CardsManager.finished = True

        return card

    @staticmethod
    def activate_card(card, player, enemy_player):
        if not ResourcesManager.can_afford_card(player.resources, card.cost):
            return False

        ResourcesManager.deduct_resources(player.resources, card.cost)

        if card.effects_on_me.get("instant"):
            CardsManager.apply_effects(player, card.effects_on_me["instant"])

        if card.effects_on_enemy.get("instant"):
            CardsManager.apply_effects(
                enemy_player, card.effects_on_enemy["instant"]
            )

        if card.yields.get("instant"):
            ResourcesManager.add_resources(
                player.resources, card.yields["instant"]
            )

        player.add_card(card)
        return True

    @staticmethod
    def process_recurring_effects(player, enemy_player):

        if player not in CardsManager.negative_resources_count:
            CardsManager.negative_resources_count[player] = 0

        for card in player.cards:
            if card.yields.get("each_turn"):
                ResourcesManager.add_resources(
                    player.resources, card.yields["each_turn"]
                )

            ResourcesManager.deduct_resources(
                player.resources, card.recurring_cost
            )

            if card.effects_on_me.get("each_turn"):
                CardsManager.apply_effects(
                    player, card.effects_on_me["each_turn"]
                )
            if card.effects_on_enemy.get("each_turn"):
                CardsManager.apply_effects(
                    enemy_player, card.effects_on_enemy["each_turn"]
                )

            if card.valid_for > 0:
                card.valid_for -= 1

        if player.resources.is_negative():
            CardsManager.negative_resources_count[player] += 1
            print(
                f"Player {player.name} has negative resources. "
                f"Count: {CardsManager.negative_resources_count[player]}"
            )
        else:
            CardsManager.negative_resources_count[player] = 0

        if CardsManager.negative_resources_count[player] >= 10:
            print(f"Player {player.name} has lost due to negative resources.")
            player.has_lost = True

    @staticmethod
    def apply_effects(player, effects):
        if "on_player" in effects:
            player.health += effects["on_player"].get("health", 0)

        if "on_monsters" in effects:
            health_effect = effects["on_monsters"].get("health", 0)
            damage_effect = effects["on_monsters"].get("damage", 0)
            num_monsters = effects["on_monsters"].get("number_of_monsters", -1)

            cards_to_affect = [
                card
                for card in player.cards
                if card.type in {"monster", "building"}
            ]

            monsters_to_affect = (
                cards_to_affect
                if num_monsters == -1
                else cards_to_affect[:num_monsters]
            )
            for monster in monsters_to_affect:
                monster.stats["health"] += health_effect
                monster.stats["damage"] += damage_effect

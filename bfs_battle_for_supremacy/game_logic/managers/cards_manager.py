from bfs_battle_for_supremacy.game_logic.entities.square import Square
from bfs_battle_for_supremacy.game_logic.utilities.ai_handler import AiHandler
from bfs_battle_for_supremacy.game_logic.managers.resources_manager import (
    ResourcesManager,
)
from bfs_battle_for_supremacy.game_logic.managers.map_manager import (
    MapManager,
)


class CardsManager:
    loading = False
    finished = False
    current_card = None
    negative_resources_count = {}

    @staticmethod
    def provide_card():
        CardsManager.loading = True

        card = AiHandler.send_card_request()
        if not card.type:
            CardsManager.loading = False
            return None

        CardsManager.current_card = card
        CardsManager.loading = False
        CardsManager.finished = True

        return card

    @staticmethod
    def activate_card(card, player, enemy_player, target_square: Square):
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
        if target_square:
            if MapManager.place_item(target_square, card):
                card.location = target_square
                player.add_card(card)
                return True
            return False
        return True

    @staticmethod
    def process_recurring_effects(player, enemy_player):
        results = []

        if player not in CardsManager.negative_resources_count:
            CardsManager.negative_resources_count[player] = 0
        if enemy_player not in CardsManager.negative_resources_count:
            CardsManager.negative_resources_count[enemy_player] = 0

        for card in player.cards:
            if card.yields.get("each_turn"):
                ResourcesManager.add_resources(
                    player.resources, card.yields["each_turn"]
                )
                results.append(
                    f"Card {card.title} generated resources: "
                    + f"{card.yields['each_turn']}."
                )

            ResourcesManager.deduct_resources(
                player.resources, card.recurring_cost
            )
            results.append(
                f"Card {card.title} deducted resources: {card.recurring_cost}."
            )

            if card.effects_on_me.get("each_turn"):
                CardsManager.apply_effects(
                    player, card.effects_on_me["each_turn"]
                )
                results.append(
                    f"Card {card.title} applied effects on player: "
                    + f"{card.effects_on_me['each_turn']}."
                )
            if card.effects_on_enemy.get("each_turn"):
                CardsManager.apply_effects(
                    enemy_player, card.effects_on_enemy["each_turn"]
                )
                results.append(
                    f"Card {card.title} applied effects on enemy: "
                    + f"{card.effects_on_enemy['each_turn']}."
                )

            if card.valid_for > 0:
                card.valid_for -= 1
                results.append(
                    f"Card {card.title} validity reduced to {card.valid_for}."
                )

        if player.resources.is_negative():
            CardsManager.negative_resources_count[player] += 1
            results.append(
                f"Player {player.name} has negative resources. "
                f"Count: {CardsManager.negative_resources_count[player]}."
            )
        else:
            CardsManager.negative_resources_count[player] = 0

        if CardsManager.negative_resources_count[player] >= 10:
            player.has_lost = True
            results.append(
                f"Player {player.name} has lost due to negative resources."
            )

        if enemy_player.resources.is_negative():
            CardsManager.negative_resources_count[enemy_player] += 1
            results.append(
                f"Enemy Player {enemy_player.name} has negative resources. "
                f"Count: {CardsManager.negative_resources_count[enemy_player]}"
            )
        else:
            CardsManager.negative_resources_count[enemy_player] = 0

        if CardsManager.negative_resources_count[enemy_player] >= 10:
            enemy_player.has_lost = True
            results.append(
                f"Enemy Player {enemy_player.name} "
                + "has lost due to negative resources."
            )

        return results

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
            for card in monsters_to_affect:
                card.health += health_effect
                card.damage += damage_effect
                print(
                    f"{card.title} health updated to {card.health}, "
                    f"damage updated to {card.damage}."
                )

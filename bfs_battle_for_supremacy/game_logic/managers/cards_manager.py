from bfs_battle_for_supremacy.game_logic.entities.card import Card
from bfs_battle_for_supremacy.game_logic.entities.monster import Monster
from bfs_battle_for_supremacy.game_logic.entities.building import Building
from bfs_battle_for_supremacy.game_logic.utilities.ai_handler import AiHandler
from bfs_battle_for_supremacy.game_logic.managers.resources_manager import ResourcesManager
from bfs_battle_for_supremacy.game_logic.entities.resources import Resources


class CardsManager:
    loading = False
    finished = False
    current_card = None

    @staticmethod
    def provide_card(player):
        CardsManager.loading = True

        card_data = AiHandler.send_card_request()
        print(f"Card data received: {card_data}")

        card_type = card_data.get("type")
        if not card_type:
            print("Error: Card type not provided.") 
            CardsManager.loading = False
            return None 

        print(f"Card type: {card_type}")

        if card_type == "monster":
            card = Monster(**card_data)
        elif card_type == "building":
            card = Building(**card_data)
        else:
            card = Card(**card_data)

        CardsManager.current_card = card
        CardsManager.loading = False
        CardsManager.finished = True

        print(f"Card provided: {card.title} of type {card_type}")
        return card



    @staticmethod
    def activate_card(card, player, enemy_player):
        if not ResourcesManager.can_afford_card(player.resources, card.consumes.get("instant")):
            return False
        
        ResourcesManager.deduct_resources(player.resources, card.consumes["instant"])

        if isinstance(card, Monster) or isinstance(card, Card) and card.type == "effect":
            if card.effects_on_me.get("instant"):
                CardsManager.apply_effects(player, card.effects_on_me["instant"])
            if card.effects_on_enemy.get("instant"):
                CardsManager.apply_effects(enemy_player, card.effects_on_enemy["instant"])

        elif isinstance(card, Building):
            if card.yields.get("instant"):
                ResourcesManager.add_resources(player.resources, card.yields["instant"])
        
        player.add_card(card)
        return True

    @staticmethod
    def process_recurring_effects(player, enemy_player):
        expired_cards = []

        for card in player.cards:
            if isinstance(card, Monster) or (isinstance(card, Card) and card.type == "effect"):
                if card.effects_on_me.get("each_turn"):
                    print(f"Applying each_turn effects on player: {card.effects_on_me['each_turn']}")  
                    CardsManager.apply_effects(player, card.effects_on_me["each_turn"])

                if card.effects_on_enemy.get("each_turn"):
                    print(f"Applying each_turn effects on enemy: {card.effects_on_enemy['each_turn']}")  
                    CardsManager.apply_effects(enemy_player, card.effects_on_enemy["each_turn"])

            elif isinstance(card, Building):
                if card.yields.get("each_turn"):
                    print(f"Yielding each_turn resources: {card.yields['each_turn']}")
                    ResourcesManager.add_resources(player.resources, Resources(**card.yields["each_turn"]))

                if not ResourcesManager.can_afford_card(player.resources, card.consumes["each_turn"]):
                    print(f"Player cannot afford card: {card.title}. Expiring card.")  
                    expired_cards.append(card)
                    continue

                ResourcesManager.deduct_resources(player.resources, card.consumes["each_turn"])

            if card.valid_for > 0:
                card.valid_for -= 1
            
            card.number_of_uses -= 1

            if card.valid_for == 0 or card.number_of_uses == 0:
                print(f"Card expired: {card.title}")
                expired_cards.append(card)

        for card in expired_cards:
            print(f"Removing expired card: {card.title}")
            player.cards.remove(card)
            if isinstance(card, Monster):
                player.monsters.remove(card)
            elif isinstance(card, Building):
                player.buildings.remove(card)




    @staticmethod
    def apply_effects(player, effects):
        print(f"Applying effects: {effects}") 
        if "on_player" in effects:
            player.health += effects["on_player"].get("health", 0)
        
        if "on_monsters" in effects:
            health_effect = effects["on_monsters"].get("health", 0)
            damage_effect = effects["on_monsters"].get("damage", 0)
            num_monsters = effects["on_monsters"].get("number_of_monsters", -1)
            
            monsters_to_affect = player.monsters if num_monsters == -1 else player.monsters[:num_monsters]
            for monster in monsters_to_affect:
                monster.health += health_effect
                monster.damage += damage_effect

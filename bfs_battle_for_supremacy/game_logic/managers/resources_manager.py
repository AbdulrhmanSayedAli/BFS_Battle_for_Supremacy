from bfs_battle_for_supremacy.game_logic.entities.resources import Resources

class ResourcesManager:

    @staticmethod
    def can_afford_card(player_resources: Resources, card_cost: Resources):
        return player_resources.can_afford(card_cost)

    @staticmethod
    def deduct_resources(player_resources: Resources, cost: Resources):
        if ResourcesManager.can_afford_card(player_resources, cost):
            player_resources.deduct(cost)

    @staticmethod
    def add_resources(player_resources: Resources, yields: Resources):
        if isinstance(yields, dict):
            yields = Resources(**yields)  
        player_resources.food += yields.food
        player_resources.wood += yields.wood
        player_resources.iron += yields.iron
        player_resources.coins += yields.coins
        ResourcesManager.ensure_no_negative(player_resources)

    @staticmethod
    def ensure_no_negative(player_resources: Resources):
        player_resources.food = max(player_resources.food, 0)
        player_resources.wood = max(player_resources.wood, 0)
        player_resources.iron = max(player_resources.iron, 0)
        player_resources.coins = max(player_resources.coins, 0)

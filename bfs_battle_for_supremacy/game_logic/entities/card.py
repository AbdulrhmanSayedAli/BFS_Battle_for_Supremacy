from bfs_battle_for_supremacy.game_logic.entities.resources import Resources
from bfs_battle_for_supremacy.game_logic.entities.square import Square

class Card:
    def __init__(self, title, description, ability, type, valid_for, rarity, number_of_uses, yields, consumes, location: Square = None, stats=None, effects_on_me=None, effects_on_enemy=None):
        self.title = title
        self.description = description
        self.ability = ability
        self.type = type
        self.valid_for = valid_for
        self.rarity = rarity
        self.number_of_uses = number_of_uses
        self.yields = yields
        self.consumes = consumes
        self.location = location 
        self.cost = Resources(**consumes.get("instant", {})) 
        self.recurring_cost = Resources(**consumes.get("each_turn", {})) 
        self.stats = stats or {}
        self.effects_on_me = effects_on_me or {}
        self.effects_on_enemy = effects_on_enemy or {}

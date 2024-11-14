from bfs_battle_for_supremacy.game_logic.entities.card import Card

class Building(Card):
    def __init__(self, title, description, ability, yields, valid_for, rarity, number_of_uses, consumes, **kwargs):
        kwargs.pop('type', None)
        super().__init__(title=title, description=description, ability=ability, valid_for=valid_for,
                         rarity=rarity, number_of_uses=number_of_uses, yields=yields, consumes=consumes,
                         type="building", **kwargs)
        self.yields = yields

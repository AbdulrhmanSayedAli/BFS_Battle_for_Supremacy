from bfs_battle_for_supremacy.game_logic.entities.resources import Resources
from bfs_battle_for_supremacy.game_logic.entities.square import Square
from bfs_battle_for_supremacy.game_logic.entities.card import Card


class Player:
    def __init__(self, name, health=100, position: Square = None):
        self.name = name
        self.health = health
        self.cards = []
        self.resources = Resources()
        self.monsters = []
        self.buildings = []
        self.position = position
        self.has_lost = False

    def add_card(self, card: Card):
        self.cards.append(card)

        if card.type == "Monster":
            self.monsters.append(card)
        elif card.type == "Building":
            self.buildings.append(card)

from bfs_battle_for_supremacy.cards.parser import CardsParser
import random


class AiHandler:
    @staticmethod
    def send_card_request():
        cards = CardsParser.getCardsList()
        card = random.choice(cards)
        return card

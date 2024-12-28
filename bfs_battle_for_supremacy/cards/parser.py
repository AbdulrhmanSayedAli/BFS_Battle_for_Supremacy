from bfs_battle_for_supremacy.game_logic.entities.card import Card
from bfs_battle_for_supremacy.cards.cards import CARDS_LIST
from bfs_battle_for_supremacy.config import IMAGES_PATH
import os


class CardsParser:
    cards: list[Card] = []

    @staticmethod
    def _parse_cards():
        for card_json in CARDS_LIST:
            print(card_json)
            image = card_json.get("image", "common_image.webp")
            image = os.path.join(IMAGES_PATH, image)
            CardsParser.cards.append(
                Card(
                    **{
                        **card_json,
                        "image": image,
                    }
                )
            )

    @staticmethod
    def getCardsList() -> list[Card]:
        if CardsParser.cards:
            return CardsParser.cards

        CardsParser._parse_cards()
        return CardsParser.cards

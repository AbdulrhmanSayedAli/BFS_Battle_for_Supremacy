class AiHandler:
    @staticmethod
    def send_card_request():
        card_data = {
            "title": "Dragon",
            "description": "A powerful dragon that can breathe fire.",
            "ability": "Fire Breath",
            "type": "monster",
            "valid_for": -1,
            "rarity": "epic",
            "number_of_uses": 1,
            "yields": {
                "each_turn": {"food": 1, "wood": 2, "iron": 0, "coins": 3},
                "instant": {"food": 0, "wood": 5, "iron": 0, "coins": 10}
            },
            "consumes": {
                "each_turn": {"food": 1, "wood": 1, "iron": 0, "coins": 2},
                "instant": {"food": 5, "wood": 5, "iron": 0, "coins": 5}
            },
            "stats": {"health": 50, "damage": 15},
            "effects_on_me": {
                "each_turn": {"on_player": {"health": 2}, "on_monsters": {"health": 1, "damage": 1, "number_of_monsters": -1}},
                "instant": {"on_player": {"health": 5}, "on_monsters": {"health": 10, "damage": 5, "number_of_monsters": -1}}
            },
            "effects_on_enemy": {
                "each_turn": {"on_player": {"health": -2}, "on_monsters": {"health": -1, "damage": -1, "number_of_monsters": -1}},
                "instant": {"on_player": {"health": -5}, "on_monsters": {"health": -10, "damage": -10, "number_of_monsters": -1}}
            }
        }
        
        print(f"Generated card data: {card_data}")  
        return card_data

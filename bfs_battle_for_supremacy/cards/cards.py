CARDS_LIST = [
    {
        "title": "Inferno Siege Tower",
        "description": "A towering building capable of launching fiery projectiles. It generates resources while dealing damage to the enemy.",
        "ability": "Deals 2 damage to all enemy monsters each turn.",
        "type": "building",
        "rarity": "epic",
        "yeilds": {
            "each_turn": {"food": 1, "wood": 3, "iron": 2, "coins": 1},
            "instant": {"food": 0, "wood": 0, "iron": 0, "coins": 0},
        },
        "consumes": {
            "each_turn": {"food": 1, "wood": 1, "iron": 0, "coins": 0},
            "instant": {"food": 0, "wood": 0, "iron": 0, "coins": 0},
        },
        "stats": {"health": 75, "damage": 0},
        "effects_on_me": {
            "each_turn": {
                "on_player": {"health": 0},
                "on_monsters": {
                    "health": 0,
                    "damage": 0,
                },
            },
            "instant": {
                "on_player": {"health": 0},
                "on_monsters": {
                    "health": 0,
                    "damage": 0,
                },
            },
        },
        "effects_on_enemy": {
            "each_turn": {
                "on_player": {"health": 0},
                "on_monsters": {
                    "health": -2,
                    "damage": 0,
                },
            },
            "instant": {
                "on_player": {"health": 0},
                "on_monsters": {
                    "health": 0,
                    "damage": 0,
                },
            },
        },
    },
    {
        "title": "Lumberjack's Hut",
        "description": "A simple building where wood is steadily gathered each turn.",
        "ability": "Generates wood each turn to support your resources.",
        "type": "building",
        "rarity": "common",
        "yeilds": {
            "each_turn": {"food": 0, "wood": 3, "iron": 0, "coins": 0},
            "instant": {"food": 0, "wood": 0, "iron": 0, "coins": 0},
        },
        "consumes": {
            "each_turn": {"food": 1, "wood": 0, "iron": 0, "coins": 0},
            "instant": {"food": 0, "wood": 0, "iron": 0, "coins": 0},
        },
        "stats": {"health": 30, "damage": 0},
        "effects_on_me": {
            "each_turn": {
                "on_player": {"health": 0},
                "on_monsters": {"health": 0, "damage": 0},
            },
            "instant": {
                "on_player": {"health": 0},
                "on_monsters": {"health": 0, "damage": 0},
            },
        },
        "effects_on_enemy": {
            "each_turn": {
                "on_player": {"health": 0},
                "on_monsters": {"health": 0, "damage": 0},
            },
            "instant": {
                "on_player": {"health": 0},
                "on_monsters": {"health": 0, "damage": 0},
            },
        },
    },
    {
        "title": "Village Healer",
        "description": "A kind soul who provides minor healing to the player and their monsters each turn.",
        "ability": "Restores health to the player and their monsters over time.",
        "type": "effect",
        "rarity": "common",
        "yeilds": {
            "each_turn": {"food": 0, "wood": 0, "iron": 0, "coins": 0},
            "instant": {"food": 0, "wood": 0, "iron": 0, "coins": 0},
        },
        "consumes": {
            "each_turn": {"food": 1, "wood": 0, "iron": 0, "coins": 1},
            "instant": {"food": 0, "wood": 0, "iron": 0, "coins": 0},
        },
        "stats": {"health": 0, "damage": 0},
        "effects_on_me": {
            "each_turn": {
                "on_player": {"health": 2},
                "on_monsters": {"health": 1, "damage": 0},
            },
            "instant": {
                "on_player": {"health": 0},
                "on_monsters": {"health": 0, "damage": 0},
            },
        },
        "effects_on_enemy": {
            "each_turn": {
                "on_player": {"health": 0},
                "on_monsters": {"health": 0, "damage": 0},
            },
            "instant": {
                "on_player": {"health": 0},
                "on_monsters": {"health": 0, "damage": 0},
            },
        },
    },
    {
        "title": "Iron Mine",
        "description": "A sturdy mine that provides a steady supply of iron each turn.",
        "ability": "Generates iron resources to fuel your needs.",
        "type": "building",
        "rarity": "common",
        "yeilds": {
            "each_turn": {"food": 0, "wood": 0, "iron": 2, "coins": 0},
            "instant": {"food": 0, "wood": 0, "iron": 0, "coins": 0},
        },
        "consumes": {
            "each_turn": {"food": 1, "wood": 0, "iron": 0, "coins": 1},
            "instant": {"food": 0, "wood": 0, "iron": 0, "coins": 0},
        },
        "stats": {"health": 40, "damage": 0},
        "effects_on_me": {
            "each_turn": {
                "on_player": {"health": 0},
                "on_monsters": {"health": 0, "damage": 0},
            },
            "instant": {
                "on_player": {"health": 0},
                "on_monsters": {"health": 0, "damage": 0},
            },
        },
        "effects_on_enemy": {
            "each_turn": {
                "on_player": {"health": 0},
                "on_monsters": {"health": 0, "damage": 0},
            },
            "instant": {
                "on_player": {"health": 0},
                "on_monsters": {"health": 0, "damage": 0},
            },
        },
    },
    {
        "title": "Farmer's Field",
        "description": "A fertile field tended by farmers, producing food each turn.",
        "ability": "Provides a consistent supply of food for your resources.",
        "type": "building",
        "rarity": "common",
        "yeilds": {
            "each_turn": {"food": 3, "wood": 0, "iron": 0, "coins": 0},
            "instant": {"food": 0, "wood": 0, "iron": 0, "coins": 0},
        },
        "consumes": {
            "each_turn": {"food": 0, "wood": 1, "iron": 0, "coins": 1},
            "instant": {"food": 0, "wood": 0, "iron": 0, "coins": 0},
        },
        "stats": {"health": 25, "damage": 0},
        "effects_on_me": {
            "each_turn": {
                "on_player": {"health": 0},
                "on_monsters": {"health": 0, "damage": 0},
            },
            "instant": {
                "on_player": {"health": 0},
                "on_monsters": {"health": 0, "damage": 0},
            },
        },
        "effects_on_enemy": {
            "each_turn": {
                "on_player": {"health": 0},
                "on_monsters": {"health": 0, "damage": 0},
            },
            "instant": {
                "on_player": {"health": 0},
                "on_monsters": {"health": 0, "damage": 0},
            },
        },
    },
    {
        "title": "Coin Vault",
        "description": "A secure vault that steadily generates coins each turn.",
        "ability": "Provides a small but reliable income of coins to support your economy.",
        "type": "building",
        "rarity": "common",
        "yeilds": {
            "each_turn": {"food": 0, "wood": 0, "iron": 0, "coins": 2},
            "instant": {"food": 0, "wood": 0, "iron": 0, "coins": 0},
        },
        "consumes": {
            "each_turn": {"food": 0, "wood": 1, "iron": 0, "coins": 0},
            "instant": {"food": 0, "wood": 0, "iron": 0, "coins": 0},
        },
        "stats": {"health": 35, "damage": 0},
        "effects_on_me": {
            "each_turn": {
                "on_player": {"health": 0},
                "on_monsters": {"health": 0, "damage": 0},
            },
            "instant": {
                "on_player": {"health": 0},
                "on_monsters": {"health": 0, "damage": 0},
            },
        },
        "effects_on_enemy": {
            "each_turn": {
                "on_player": {"health": 0},
                "on_monsters": {"health": 0, "damage": 0},
            },
            "instant": {
                "on_player": {"health": 0},
                "on_monsters": {"health": 0, "damage": 0},
            },
        },
    },
    {
        "title": "Forest Goblin",
        "description": "A mischievous creature that lurks in the forest, striking from the shadows.",
        "ability": "Deals damage to enemies with swift strikes.",
        "type": "monster",
        "rarity": "common",
        "yeilds": {
            "each_turn": {"food": 0, "wood": 0, "iron": 0, "coins": 0},
            "instant": {"food": 0, "wood": 0, "iron": 0, "coins": 0},
        },
        "consumes": {
            "each_turn": {"food": 0, "wood": 0, "iron": 0, "coins": 0},
            "instant": {"food": 0, "wood": 0, "iron": 0, "coins": 0},
        },
        "stats": {"health": 15, "damage": 5},
        "effects_on_me": {
            "each_turn": {
                "on_player": {"health": 0},
                "on_monsters": {"health": 0, "damage": 0},
            },
            "instant": {
                "on_player": {"health": 0},
                "on_monsters": {"health": 0, "damage": 0},
            },
        },
        "effects_on_enemy": {
            "each_turn": {
                "on_player": {"health": 0},
                "on_monsters": {"health": -1, "damage": 0},
            },
            "instant": {
                "on_player": {"health": -3},
                "on_monsters": {"health": -5, "damage": 0},
            },
        },
    },
    {
        "title": "Weathered Tactics",
        "description": "A quick burst of tactical insight that increases the damage of your monsters for a short time.",
        "ability": "Boosts the damage of all your monsters.",
        "type": "effect",
        "rarity": "common",
        "yeilds": {
            "each_turn": {"food": 0, "wood": 0, "iron": 0, "coins": 0},
            "instant": {"food": 0, "wood": 0, "iron": 0, "coins": 0},
        },
        "consumes": {
            "each_turn": {"food": 0, "wood": 0, "iron": 0, "coins": 1},
            "instant": {"food": 0, "wood": 0, "iron": 0, "coins": 1},
        },
        "stats": {"health": 0, "damage": 0},
        "effects_on_me": {
            "each_turn": {
                "on_player": {"health": 0},
                "on_monsters": {"health": 0, "damage": 0},
            },
            "instant": {
                "on_player": {"health": 0},
                "on_monsters": {"health": 0, "damage": 5},
            },
        },
        "effects_on_enemy": {
            "each_turn": {
                "on_player": {"health": 0},
                "on_monsters": {"health": 0, "damage": 0},
            },
            "instant": {
                "on_player": {"health": 0},
                "on_monsters": {"health": 0, "damage": 0},
            },
        },
    },
    {
        "title": "Quick Harvest",
        "description": "A sudden burst of resource gathering, giving you a temporary boost in food production.",
        "ability": "Instantly generates a burst of food to help you sustain your forces.",
        "type": "effect",
        "rarity": "common",
        "yeilds": {
            "each_turn": {"food": 0, "wood": 0, "iron": 0, "coins": 0},
            "instant": {"food": 10, "wood": 0, "iron": 0, "coins": 0},
        },
        "consumes": {
            "each_turn": {"food": 0, "wood": 0, "iron": 0, "coins": 1},
            "instant": {"food": 0, "wood": 0, "iron": 0, "coins": 1},
        },
        "stats": {"health": 0, "damage": 0},
        "effects_on_me": {
            "each_turn": {
                "on_player": {"health": 0},
                "on_monsters": {"health": 0, "damage": 0},
            },
            "instant": {
                "on_player": {"health": 0},
                "on_monsters": {"health": 0, "damage": 0},
            },
        },
        "effects_on_enemy": {
            "each_turn": {
                "on_player": {"health": 0},
                "on_monsters": {"health": 0, "damage": 0},
            },
            "instant": {
                "on_player": {"health": 0},
                "on_monsters": {"health": 0, "damage": 0},
            },
        },
    },
    {
        "title": "Sawmill",
        "description": "A sawmill that cuts logs into usable wood, providing a steady supply of wood each turn.",
        "ability": "Generates wood to support building and crafting needs.",
        "type": "building",
        "rarity": "common",
        "yeilds": {
            "each_turn": {"food": 0, "wood": 3, "iron": 0, "coins": 0},
            "instant": {"food": 0, "wood": 0, "iron": 0, "coins": 0},
        },
        "consumes": {
            "each_turn": {"food": 0, "wood": 1, "iron": 0, "coins": 0},
            "instant": {"food": 0, "wood": 0, "iron": 0, "coins": 0},
        },
        "stats": {"health": 30, "damage": 0},
        "effects_on_me": {
            "each_turn": {
                "on_player": {"health": 0},
                "on_monsters": {"health": 0, "damage": 0},
            },
            "instant": {
                "on_player": {"health": 0},
                "on_monsters": {"health": 0, "damage": 0},
            },
        },
        "effects_on_enemy": {
            "each_turn": {
                "on_player": {"health": 0},
                "on_monsters": {"health": 0, "damage": 0},
            },
            "instant": {
                "on_player": {"health": 0},
                "on_monsters": {"health": 0, "damage": 0},
            },
        },
    },
    {
        "title": "Wolf Pack",
        "description": "A group of wild wolves that hunt in packs, striking fear into their enemies with their coordinated attacks.",
        "ability": "The wolf pack deals damage in quick succession, overwhelming their enemies.",
        "type": "monster",
        "rarity": "common",
        "yeilds": {
            "each_turn": {"food": 0, "wood": 0, "iron": 0, "coins": 0},
            "instant": {"food": 0, "wood": 0, "iron": 0, "coins": 0},
        },
        "consumes": {
            "each_turn": {"food": 0, "wood": 0, "iron": 0, "coins": 0},
            "instant": {"food": 0, "wood": 0, "iron": 0, "coins": 0},
        },
        "stats": {"health": 20, "damage": 6},
        "effects_on_me": {
            "each_turn": {
                "on_player": {"health": 0},
                "on_monsters": {"health": 0, "damage": 0},
            },
            "instant": {
                "on_player": {"health": 0},
                "on_monsters": {"health": 0, "damage": 0},
            },
        },
        "effects_on_enemy": {
            "each_turn": {
                "on_player": {"health": 0},
                "on_monsters": {"health": -1, "damage": 0},
            },
            "instant": {
                "on_player": {"health": -4},
                "on_monsters": {"health": -6, "damage": 0},
            },
        },
    },
    {
        "title": "Ancient Forge",
        "description": "A long-forgotten forge, capable of crafting powerful weapons and tools from the finest metals.",
        "ability": "Boosts the damage of all monsters by enhancing their strength with crafted weapons.",
        "type": "building",
        "rarity": "rare",
        "yeilds": {
            "each_turn": {"food": 0, "wood": 0, "iron": 2, "coins": 1},
            "instant": {"food": 0, "wood": 0, "iron": 5, "coins": 0},
        },
        "consumes": {
            "each_turn": {"food": 0, "wood": 0, "iron": 1, "coins": 1},
            "instant": {"food": 0, "wood": 0, "iron": 2, "coins": 1},
        },
        "stats": {"health": 40, "damage": 0},
        "effects_on_me": {
            "each_turn": {
                "on_player": {"health": 0},
                "on_monsters": {"health": 0, "damage": 0},
            },
            "instant": {
                "on_player": {"health": 0},
                "on_monsters": {"health": 0, "damage": 5},
            },
        },
        "effects_on_enemy": {
            "each_turn": {
                "on_player": {"health": 0},
                "on_monsters": {"health": 0, "damage": 0},
            },
            "instant": {
                "on_player": {"health": 0},
                "on_monsters": {"health": -3, "damage": 0},
            },
        },
    },
    {
        "title": "Mystic Elixir",
        "description": "A potent brew that enhances the health and combat abilities of your monsters.",
        "ability": "Boosts the health and damage of all your monsters.",
        "type": "effect",
        "rarity": "rare",
        "yeilds": {
            "each_turn": {"food": 0, "wood": 0, "iron": 0, "coins": 0},
            "instant": {"food": 0, "wood": 0, "iron": 0, "coins": 0},
        },
        "consumes": {
            "each_turn": {"food": 0, "wood": 0, "iron": 0, "coins": 2},
            "instant": {"food": 0, "wood": 0, "iron": 0, "coins": 2},
        },
        "stats": {"health": 0, "damage": 0},
        "effects_on_me": {
            "each_turn": {
                "on_player": {"health": 0},
                "on_monsters": {"health": 0, "damage": 0},
            },
            "instant": {
                "on_player": {"health": 0},
                "on_monsters": {"health": 10, "damage": 5},
            },
        },
        "effects_on_enemy": {
            "each_turn": {
                "on_player": {"health": 0},
                "on_monsters": {"health": 0, "damage": 0},
            },
            "instant": {
                "on_player": {"health": 0},
                "on_monsters": {"health": -5, "damage": -3},
            },
        },
    },
    {
        "title": "Arcane Storm",
        "description": "A powerful magical storm that strikes the enemy with devastating force, disrupting their plans.",
        "ability": "Deals damage to all enemy monsters and reduces their damage.",
        "type": "effect",
        "rarity": "rare",
        "yeilds": {
            "each_turn": {"food": 0, "wood": 0, "iron": 0, "coins": 0},
            "instant": {"food": 0, "wood": 0, "iron": 0, "coins": 0},
        },
        "consumes": {
            "each_turn": {"food": 0, "wood": 0, "iron": 0, "coins": 2},
            "instant": {"food": 0, "wood": 0, "iron": 0, "coins": 2},
        },
        "stats": {"health": 0, "damage": 0},
        "effects_on_me": {
            "each_turn": {
                "on_player": {"health": 0},
                "on_monsters": {"health": 0, "damage": 0},
            },
            "instant": {
                "on_player": {"health": 0},
                "on_monsters": {"health": 0, "damage": 0},
            },
        },
        "effects_on_enemy": {
            "each_turn": {
                "on_player": {"health": 0},
                "on_monsters": {"health": 0, "damage": 0},
            },
            "instant": {
                "on_player": {"health": 0},
                "on_monsters": {"health": -6, "damage": -4},
            },
        },
    },
    {
        "title": "Thunder Dragon",
        "description": "A majestic dragon who commands the power of lightning, striking down enemies with electrifying fury.",
        "ability": "Deals heavy damage and stuns enemy monsters, reducing their damage output.",
        "type": "monster",
        "rarity": "rare",
        "yeilds": {
            "each_turn": {"food": 0, "wood": 0, "iron": 0, "coins": 0},
            "instant": {"food": 0, "wood": 0, "iron": 0, "coins": 0},
        },
        "consumes": {
            "each_turn": {"food": 1, "wood": 0, "iron": 0, "coins": 1},
            "instant": {"food": 0, "wood": 0, "iron": 0, "coins": 2},
        },
        "stats": {"health": 50, "damage": 15},
        "effects_on_me": {
            "each_turn": {
                "on_player": {"health": 0},
                "on_monsters": {"health": 0, "damage": 0},
            },
            "instant": {
                "on_player": {"health": 0},
                "on_monsters": {"health": 0, "damage": 0},
            },
        },
        "effects_on_enemy": {
            "each_turn": {
                "on_player": {"health": 0},
                "on_monsters": {"health": 0, "damage": 0},
            },
            "instant": {
                "on_player": {"health": 0},
                "on_monsters": {"health": -10, "damage": -5},
            },
        },
    },
    {
        "title": "Vampire's Curse",
        "description": "A dark curse that drains the life force from your enemies, healing your monsters in the process.",
        "ability": "Deals damage to all enemy monsters and restores health to your monsters based on the damage dealt.",
        "type": "effect",
        "rarity": "rare",
        "yeilds": {
            "each_turn": {"food": 0, "wood": 0, "iron": 0, "coins": 0},
            "instant": {"food": 0, "wood": 0, "iron": 0, "coins": 0},
        },
        "consumes": {
            "each_turn": {"food": 0, "wood": 0, "iron": 0, "coins": 3},
            "instant": {"food": 0, "wood": 0, "iron": 0, "coins": 3},
        },
        "stats": {"health": 0, "damage": 0},
        "effects_on_me": {
            "each_turn": {
                "on_player": {"health": 0},
                "on_monsters": {"health": 0, "damage": 0},
            },
            "instant": {
                "on_player": {"health": 0},
                "on_monsters": {"health": 5, "damage": 0},
            },
        },
        "effects_on_enemy": {
            "each_turn": {
                "on_player": {"health": 0},
                "on_monsters": {"health": -4, "damage": 0},
            },
            "instant": {
                "on_player": {"health": 0},
                "on_monsters": {"health": -8, "damage": 0},
            },
        },
    },
]

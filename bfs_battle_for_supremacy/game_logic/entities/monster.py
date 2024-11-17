from bfs_battle_for_supremacy.game_logic.entities.card import Card


class Monster(Card):
    def __init__(
        self,
        title,
        description,
        ability,
        stats,
        valid_for,
        rarity,
        number_of_uses,
        yields,
        consumes,
        **kwargs,
    ):
        kwargs.pop("type", None)
        super().__init__(
            title=title,
            description=description,
            ability=ability,
            valid_for=valid_for,
            rarity=rarity,
            number_of_uses=number_of_uses,
            yields=yields,
            consumes=consumes,
            stats=stats,
            type="monster",
            **kwargs,
        )
        self.health = stats.get("health", 0)
        self.damage = stats.get("damage", 0)

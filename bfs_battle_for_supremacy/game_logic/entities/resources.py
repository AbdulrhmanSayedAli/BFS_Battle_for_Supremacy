class Resources:
    def __init__(self, food=100, wood=100, iron=100, coins=100):
        self.food = food
        self.wood = wood
        self.iron = iron
        self.coins = coins

    def deduct(self, other):
        if isinstance(other, dict):
            other = Resources(**other)
        self.food -= other.food
        self.wood -= other.wood
        self.iron -= other.iron
        self.coins -= other.coins
        self.ensure_non_negative()

    def add(self, other):
        if isinstance(other, dict):
            other = Resources(**other)
        self.food += other.food
        self.wood += other.wood
        self.iron += other.iron
        self.coins += other.coins

    def can_afford(self, other):
        if isinstance(other, dict):
            other = Resources(**other)
        return (
            self.food >= other.food
            and self.wood >= other.wood
            and self.iron >= other.iron
            and self.coins >= other.coins
        )

    def ensure_non_negative(self):
        self.food = max(self.food, 0)
        self.wood = max(self.wood, 0)
        self.iron = max(self.iron, 0)
        self.coins = max(self.coins, 0)

    def is_negative(self):
        return (
            self.food < 0 or self.wood < 0 or self.iron < 0 or self.coins < 0
        )

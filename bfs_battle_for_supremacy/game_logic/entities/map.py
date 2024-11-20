from .square import Square


class Map:
    def __init__(self, rows, columns):
        self.grid = [
            [Square(row, col) for col in range(columns)] for row in range(rows)
        ]

    def get_square(self, row, col):
        if 0 <= row < len(self.grid) and 0 <= col < len(self.grid[0]):
            return self.grid[row][col]
        return None

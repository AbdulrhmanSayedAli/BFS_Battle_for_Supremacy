from .square import Square


class Map:
    def __init__(self, rows, columns):
        self.grid = [
            [Square(row, col) for col in range(columns)] for row in range(rows)
        ]

    def get_square(self, row, col):
        return self.grid[row][col]

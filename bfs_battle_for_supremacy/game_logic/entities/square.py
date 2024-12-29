class Square:
    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.is_empty = True
        self.content = None

    def set_content(self, content):
        self.content = content
        self.is_empty = False if content else True

    def clear_content(self):
        self.content = None
        self.is_empty = True

    def get_content(self):
        return self.content

    def __str__(self):
        return f"{self.row} {self.column}"

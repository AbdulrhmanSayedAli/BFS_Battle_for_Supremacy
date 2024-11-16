class Rock:
    def __init__(self, image_path):
        self.name = "Rock"
        self.image_path = image_path

    def __repr__(self):
        return f"<Rock: {self.name}>"

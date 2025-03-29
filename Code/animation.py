class Animation:
    def __init__(self, position: tuple):
        self.right = [pygame.image.load(f".assets/Entidades/Run{i}.png") for i in range(1, 8)]

    def run(self):
        pass
import pyray

from objects.texture import Image


class Cherry(Image):
    def __init__(self, game, textures, rect: pyray.Rectangle, weight: int) -> None:
        super().__init__(game, textures, rect)
        self.weight = weight
        self.eaten = False
        self.radius = 0
        self.coordinate = [rect.x, rect.y]

    def show(self):
        self.radius = 12

    def hide(self):
        self.radius = 0

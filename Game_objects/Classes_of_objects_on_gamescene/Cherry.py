import pyray
from raylib import colors
from Game_objects.Classes_of_objects_on_gamescene.Sprite import Sprite


class Cherry(Sprite):
    def __init__(self, path: str, rect: pyray.Rectangle, weight: int) -> None:
        super().__init__(path, rect)
        self.weight = weight
        self.eaten = False
        self.radius = 0
        self.coordinate = [rect.x, rect.y]

    def show(self):
        self.radius = 12

    def hide(self):
        self.radius = 0

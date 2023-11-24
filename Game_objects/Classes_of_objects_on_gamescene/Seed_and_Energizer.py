import pyray
from Game_objects.Classes_of_objects_on_gamescene.Sprite import Sprite
# Импортим класс для создания объектов из
# Sprite.py(pacman_developer/Game_objects/Classes_of_objects_on_gamescene)
# Для получения большей информации о классе - перейдите в файл


class Seed(Sprite):
    def __init__(self, path: str,  rect: pyray.Rectangle, weight: int) -> None:
        super().__init__(path, rect)
        self.weight = weight
        self.eaten = False
        self.radius = 10
        self.coordinate = [rect.x, rect.y]


class Energizer(Seed):
    def __init__(self, path: str, rect: pyray.Rectangle, weight: int) -> None:
        super().__init__(path, rect, weight)
        self.radius = 15

import pyray
from Game_objects.Classes_of_objects_on_gamescene.Sprite import Sprite

# Импортим класс для создания объектов из
# Sprite.py(Game_objects/Classes_of_objects_on_gamescene)


class Seed(Sprite):
    def __init__(self, path: str,  rect: pyray.Rectangle, weight: int) -> None:
        super().__init__(path, rect)
        self.weight = weight  # Очки за съеденное зерно
        self.coordinate = [rect.x, rect.y]  # Координаты зерна


class Energizer(Seed):
    def __init__(self, path: str, rect: pyray.Rectangle, weight: int) -> None:
        super().__init__(path, rect, weight)

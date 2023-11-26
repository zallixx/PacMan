import pyray

from objects.texture import Image


# Импортим класс для создания объектов из
# Sprite.py(objects/Classes_of_objects_on_gamescene)


class Seed(Image):
    def __init__(self, game, texture, rect: pyray.Rectangle, weight: int) -> None:
        super().__init__(game, texture, rect)
        self.weight = weight  # Очки за съеденное зерно
        self.coordinate = [rect.x, rect.y]  # Координаты зерна


class Energizer(Seed):
    def __init__(self, game, texture, rect: pyray.Rectangle, weight: int) -> None:
        super().__init__(game, texture, rect, weight)

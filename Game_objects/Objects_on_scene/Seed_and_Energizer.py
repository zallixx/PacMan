import pyray
from Game_objects.Objects_on_scene.Base_file_for_objects import Create_Object
# Импортим класс для создания объектов из
# Base_file_for_objects.py(pacman_developer/Game_objects/Objects_on_scene)
# Для получения большей информации о классе - перейдите в файл


class Seed(Create_Object):
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

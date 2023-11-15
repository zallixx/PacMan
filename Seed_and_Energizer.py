import pyray
from Base_file_for_objects import Create_Object
# Импортим класс для создания объектов из Base_file_for_objects.py
# Для получения большей информации о классе - перейдите в его файл


class Seed(Create_Object):
    def __init__(self, path: str,  rect: pyray.Rectangle, weight: int) -> None:
        super().__init__(path, rect)
        self.weight = weight
        self.eaten = False
        self.radius = 10
        self.coordinate = [rect.x, rect.y]

    def draw(self) -> None:
        pyray.draw_circle(int(self.coordinate[0]), int(self.coordinate[1]), self.radius, pyray.YELLOW)


class Energizer(Seed):
    def __init__(self, path: str, rect: pyray.Rectangle, weight: int) -> None:
        super().__init__(path, rect, weight)
        self.radius = 15

    def draw(self) -> None:
        super().draw()

import pyray
from Game_objects.Classes_of_objects_on_gamescene.Base_file_for_objects import Create_Object
# Импортим класс(Create_Object) для создания объектов из
# Base_file_for_objects.py(pacman_developer/Game_objects/Classes_of_objects_on_gamescene)
# Для получения большей информации о классе - перейдите в файл


# Пока что передвижение призрака описывается с помощью movement_coordinate(координаты перемещения)
# А также movement_force(силой перемещения)
# C появлением алгоритма перемещения - изменить данный способ перемещения


class Ghost(Create_Object):
    def __init__(self, path: str, rect: pyray.Rectangle,
                 movement_coordinate: str, movement_force: int) -> None:
        super().__init__(path, rect)
        self.movement_coordinate = movement_coordinate
        self.movement_force = movement_force

    def event(self):
        if self.movement_coordinate == "x":
            self.coordinate[0] += self.movement_force
        elif self.movement_coordinate == "y":
            self.coordinate[1] += self.movement_force

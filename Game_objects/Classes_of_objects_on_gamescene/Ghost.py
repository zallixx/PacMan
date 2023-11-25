import pyray
from Game_objects.Classes_of_objects_on_gamescene.Sprite import Sprite
from pacman_developer.Drawing_scenes.gameoverscene import GameOverScene

# Импортим класс(Sprite) для создания объектов из
# Sprite.py(pacman_developer/Game_objects/Classes_of_objects_on_gamescene)
# Для получения большей информации о классе - перейдите в файл


# Пока что передвижение призрака описывается с помощью movement_coordinate(координаты перемещения)
# А также movement_force(силой перемещения)
# C появлением алгоритма перемещения - изменить данный способ перемещения


class Ghost(Sprite):
    def __init__(self, path: str, rect: pyray.Rectangle,
                 movement_coordinate: str, movement_force: int, game) -> None:
        super().__init__(path, rect)
        self.game = game
        self.movement_coordinate = movement_coordinate
        self.movement_force = movement_force

    def logic(self, pacman) -> None:
        ghost_rect = pyray.Rectangle(self.coordinate[0], self.coordinate[1], self.width, self.height)
        pacman_rect = pyray.Rectangle(pacman.coordinate[0], pacman.coordinate[1], pacman.width, pacman.height)
        if pyray.check_collision_recs(ghost_rect, pacman_rect):
            self.game.change_scene(GameOverScene(self.game))

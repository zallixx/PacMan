import pyray

from objects.audio import Audio
from objects.texture import Image
from scenes.gameoverscene import GameOverScene


# Импортим класс(Sprite) для создания объектов из
# Sprite.py(pacman_developer/objects/Classes_of_objects_on_gamescene)
# Для получения большей информации о классе - перейдите в файл


# Пока что передвижение призрака описывается с помощью movement_coordinate(координаты перемещения)
# А также movement_force(силой перемещения)
# C появлением алгоритма перемещения - изменить данный способ перемещения


class Ghost(Image):
    def __init__(self, game, texture, rect: pyray.Rectangle,
                 movement_coordinate: str, movement_force: int, ) -> None:
        super().__init__(game, texture, rect)
        self.death_sound = Audio(self.game, self.game.volume_level / 100, 'sounds/death_sound.wav')
        self.movement_coordinate = movement_coordinate
        self.movement_force = movement_force

    def logic(self, pacman) -> None:
        ghost_rect = pyray.Rectangle(self.rect.x, self.rect.y, self.rect.width, self.rect.height)
        pacman_rect = pyray.Rectangle(pacman.rect.x, pacman.rect.y, pacman.rect.width, pacman.rect.height)
        if pyray.check_collision_recs(ghost_rect, pacman_rect):
            self.game.life_draw.remove()
            pacman.rect.x = 409
            pacman.rect.y = 335
            pacman.future_x = 0
            pacman.future_y = 0
            pacman.shift_x = 0
            pacman.shift_y = 0

        if self.game.life_draw.lifecount == 0:
            self.game.change_scene(GameOverScene(self.game))
            self.game.life_draw.lifecount = 3
            self.death_sound.play_track()

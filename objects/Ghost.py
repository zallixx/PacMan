import pyray

from bfs import Bfs
from objects.audio import Audio
from objects.texture import Image
from scenes.gameoverscene import GameOverScene


# Импортим класс(Image) для создания объектов из
# texture.py(.../objects/texture.py)
# Для получения большей информации о классе - перейдите в файл


# Пока что передвижение призрака описывается с помощью movement_coordinate(координаты перемещения)
# А также movement_force(силой перемещения)
# C появлением алгоритма перемещения - изменить данный способ перемещения


class Ghost(Image):
    current_frame = 0
    frame_to_shift = 20

    def __init__(self, game, texture: pyray.Texture, rect: pyray.Rectangle) -> None:
        """ Класс призраков, позволяющий работать с их отрисовкой, событиями, логикой
        :param game: все переменные игры
        :type game: Game
        :param texture: текстура
        :type texture: pyray.Texture
        :param rect: положение, длина и ширина
        :type rect: pyray.Rectangle
        """
        super().__init__(game, texture, rect)
        self.death_sound = Audio(self.game, self.game.Settings.get_volume_level(), 'sounds/death_sound.wav')
        self.bfs = Bfs()

    def logic(self, pacman) -> None:
        """ Функция логики у призраков, пока что отвечает за: 1) отнятие сердец у пакмана при коллизии с призраком
        :param pacman: объект класса Pacman
        :type pacman: <class Pacman>
        :return: Null
        """
        Gx, Gy = self.game.field.coords_to_clear(
            self.rect.x, self.rect.y)
        self.bfs.logic(self.game.fieldTxt, (Gx, Gy),
                       self.game.field.coords_to_clear(pacman.rect.x, pacman.rect.y), '#')
        # print(self.bfs.path)
        # self.bfs.print_map(self.game.fieldTxt, self.bfs.path[1:-1])
        ghost_rect = pyray.Rectangle(self.rect.x, self.rect.y, self.rect.width, self.rect.height)
        pacman_rect = pyray.Rectangle(pacman.rect.x, pacman.rect.y, pacman.rect.width, pacman.rect.height)
        self.move()
        if pyray.check_collision_recs(ghost_rect, pacman_rect):
            self.game.Settings.remove_pacman_life()
            pacman.to_spawn()
        if self.game.Settings.get_pacman_lifes() == 0:
            self.game.change_scene(GameOverScene(self.game))
            self.death_sound.play_track()

    def move(self) -> None:
        """
        Движение приведения
        :return: Null
        """
        self.current_frame += 1
        if self.current_frame != self.frame_to_shift:
            return

        sxy = self.bfs.path[0]
        if len(self.bfs.path) >= 2:
            txy = self.bfs.path[1]
        else:
            return 0
        if sxy[0] == txy[0]:
            n = txy[1] - sxy[1]
            if n < 0:
                self.rect.x -= self.game.field.CELL_SIZE
            else:
                self.rect.x += self.game.field.CELL_SIZE
        elif sxy[1] == txy[1]:
            n = txy[0] - sxy[0]
            if n < 0:
                self.rect.y -= self.game.field.CELL_SIZE
            else:
                self.rect.y += self.game.field.CELL_SIZE
        self.current_frame=0

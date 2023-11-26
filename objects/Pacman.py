from objects.audio import Audio
import pyray
from objects.cells import *
from objects.texture import Image


# Импортим класс(Image) для создания объектов из
# texture.py(../objects/texture.py)
# Для получения большей информации о классе - перейдите в файл


class Pacman(Image):
    def __init__(self, game, texture: pyray.Texture, rect: pyray.Rectangle) -> None:
        """ Класс пакмана, содержит основную логику и поведение пакмана
        :param game: все переменные игры
        :type game: Game
        :param texture: текстура
        :type texture: pyray.Texture
        :param rect: положение, длина и ширина
        :type rect: pyray.Rectangle
        """
        super().__init__(game, texture, rect)
        self.shift = 1
        self.shift_x = self.shift_y = 0
        self.future_x = self.future_y = 0
        self.eat_sound = Audio(self.game, self.game.volume_level / 100, 'sounds/eat_seed_sound.wav')
        self.textures = {"UP": self.game.Textures.get_texture("images/pacmanup.png"),
                         "DOWN": self.game.Textures.get_texture("images/pacmandown.png"),
                         "LEFT": self.game.Textures.get_texture("images/pacmanleft.png"),
                         "RIGHT": self.game.Textures.get_texture("images/pacmanright.png")}

        self.directions = {
            pyray.KeyboardKey.KEY_W: {"future_y": -self.shift, "future_x": 0},
            pyray.KeyboardKey.KEY_S: {"future_y": self.shift, "future_x": 0},
            pyray.KeyboardKey.KEY_A: {"future_x": -self.shift, "future_y": 0},
            pyray.KeyboardKey.KEY_D: {"future_x": self.shift, "future_y": 0}
        }

    def event(self) -> None:
        """Обработка ивентов клавиш
        :return: Null
        """
        for key, elements in self.directions.items():
            if pyray.is_key_down(key):
                self.future_x = elements.get("future_x")
                self.future_y = elements.get("future_y")

    def move(self) -> None:
        """Движение пакмана
        :return: Null
        """
        self.rect.x += self.shift_x
        self.rect.y += self.shift_y
        self.predict_future()

    def logic(self, pacman) -> None:
        """ Обработка логики
        :param pacman: чтобы стандартизировать(костыль)
        :return: Null
        """
        next_tile = self.game.field.get_tile(*self.get_next_tile(self.shift_x, self.shift_y))
        todo = {
            Empty: self.move,
            Wall: self.process_wall,
            Teleport: self.process_teleport,
            Seed: self.process_seed,
            BigSeed: self.process_big_seed
        }
        process = todo[type(next_tile)]
        process()

    def process_seed(self) -> None:
        """ Обработка поедания зерна
        :return: Null
        """
        seed = self.game.field.get_tile(*self.get_next_tile(self.shift_x, self.shift_y))
        empty = Empty(self.game, pyray.Rectangle(seed.rect.x, seed.rect.y, seed.rect.width, seed.rect.height))
        self.game.field.set_tile_by_coords(empty)
        self.move()
        self.eat_sound.play_track()
        self.game.score_draw.add(10)
        # :TODO пофиксить баг с поеданием зёрен наперёд в направлении вправо и вниз


    def get_next_tile(self, shift_x: int, shift_y: int):
        """ Получить координаты следующей клетки по инерции пакмана
        :param shift_x: смещение по x
        :type shift_x: int
        :param shift_y: смещение по y
        :type shift_y: int

        :rtype: (int, int)
        :return: возвращает столбец и строку следующей клетки
        """
        if shift_x == 0:
            current_y = (self.rect.y - self.rect.height / 2) if shift_y <= 0 else (
                    self.rect.y + self.rect.height / 2)
            current_x = self.rect.x
        elif shift_y == 0:
            current_x = (self.rect.x - self.rect.width / 2) if shift_x <= 0 else (
                    self.rect.x + self.rect.width / 2)
            current_y = self.rect.y

        next_x = current_x + shift_x
        next_y = current_y + shift_y
        return self.game.field.coords_to_clear(next_x, next_y)

    def predict_future(self) -> None:
        """ Предсказывает поворот
        :return: Null
        """
        pacman_rect = pyray.Rectangle(self.rect.x - (self.rect.width // 2),
                                      self.rect.y - (self.rect.height // 2), self.rect.width,
                                      self.rect.height)
        tile_rect = self.game.field.get_tile_by_coords(self.rect.x, self.rect.y).rect

        if pacman_rect.x == tile_rect.x and pacman_rect.y == tile_rect.y and tile_rect.width == pacman_rect.width:
            next_tile = self.game.field.get_tile(*self.get_next_tile(self.future_x, self.future_y))
            if (type(next_tile) is not Wall) and (type(next_tile) is not Gate):
                self.shift_x = self.future_x
                self.shift_y = self.future_y
                self.rotate()

    def rotate(self) -> None:
        """Поворачивает пакмана, в зависимости от движения
        :return: Null
        """
        if self.shift_x == self.shift:
            self.texture = self.textures['RIGHT']
        elif self.shift_x == -self.shift:
            self.texture = self.textures['LEFT']
        elif self.shift_y == self.shift:
            self.texture = self.textures['DOWN']
        elif self.shift_y == -self.shift:
            self.texture = self.textures['UP']

    def process_wall(self) -> None:
        """ Обработка стены(остановка)
        :return: Null
        """
        if self.shift_x > 0 or self.shift_y > 0:
            self.move()
        self.shift_x = self.shift_y = 0

    def process_teleport(self) -> None:
        """Обработка телепорта
        :return: Null
        """
        row, col = self.get_next_tile(self.shift_x, self.shift_y)
        if col == 0:
            self.rect.x = 634 - 18
            self.rect.y = 281
        else:
            self.rect.x = 148 + 36
            self.rect.y = 281
        self.move()

    def process_big_seed(self) -> None:
        """Обработка большого зерна
        :return: Null
        """
        self.game.score_draw.add(10)
        self.process_seed()

import datetime
import pyray
from raylib import colors

from objects.texture import Image

# Импортим класс(Image) для создания объектов из
# texture.py(.../objects/texture.py)
# Для получения большей информации о классе - перейдите в файл


class Empty(Image):
    def __init__(self, game, rect: pyray.Rectangle) -> None:
        """ Класс "пустоты" на игровой сцене. Не имеет текстуры
        :param game: все переменные игры
        :type game: Game
        :param rect: положение, длина и ширина
        :type rect: pyray.Rectangle
        """
        super().__init__(game, None, rect)


class Wall(Image):
    def __init__(self, game, rect: pyray.Rectangle) -> None:
        """ Класс "стены" на игровой сцене, позволяющий отрисовывать её. Текстура - синий квадрат
        :param game: все переменные игры
        :type game: Game
        :param rect: положение, длина и ширина
        :type rect: pyray.Rectangle
        """
        super().__init__(game, None, rect)

    def draw(self) -> None:
        """ Функция отрисовки стены
        :return: Null
        """
        pyray.draw_rectangle_rec(self.rect, colors.BLUE)


class Teleport(Image):
    teleports = []

    def __init__(self, game, rect: pyray.Rectangle) -> None:
        """ Класс "телепорта" на игровой сцене, позволяющий работать с ними. Не имеет текстуры
        Класс содержит переменную teleports[] - список объектов этого же класса.
        :param game: все переменные игры
        :type game: Game
        :param rect: положение, длина и ширина
        :type rect: pyray.Rectangle
        """
        super().__init__(game, None, rect)
        self.teleports.append(self)
        self.index = len(self.teleports) - 1

    def get_next_teleport(self) -> None:
        """ Функция получения следующего телепорта
        :return: Null
        """
        return self.teleports[(self.index + 1) % len(self.teleports)]

    def draw(self) -> None:
        """ Функция отрисовки телепорта, пустая, чтобы телепорт не было видно
        :return: Null
        """
        pass


class Seed(Image):
    filename = 'images/seed.png'

    def __init__(self, game, rect: pyray.Rectangle) -> None:
        """ Класс "зерна" на игровой сцене, позволяющий работать с ними. Имеет текстуру по пути 'images/seed.png'
        Класс содержит переменную filename - путь к картинке.
        :param game: все переменные игры
        :type game: Game
        :param rect: положение, длина и ширина
        :type rect: pyray.Rectangle
        """
        super().__init__(game, game.Textures.get_texture(Seed.filename), rect)

    def draw(self) -> None:
        """ Функция отрисовки зерна
        :return: Null
        """
        source = pyray.Rectangle(0, 0, self.texture.width, self.texture.height)
        dest = pyray.Rectangle(self.rect.x + 17, self.rect.y + 18, self.texture.width, self.texture.height)
        origin = pyray.Vector2(self.rect.width // 2, self.rect.height // 2)
        pyray.draw_texture_pro(self.texture, source, dest, origin, self.rotation, pyray.WHITE)


class BigSeed(Seed):
    filename = 'images/bigseed.png'

    def __init__(self, game, rect: pyray.Rectangle) -> None:
        """ Класс "большого зерна" на игровой сцене, позволяющий работать с ними. Имеет текстуру по пути 'images/bigseed.png'
        Класс содержит переменную filename - путь к картинке.
        :param game: все переменные игры
        :type game: Game
        :param rect: положение, длина и ширина
        :type rect: pyray.Rectangle
        """
        super().__init__(game, rect)
        self.texture = self.game.Textures.get_texture(self.filename)

    def draw(self) -> None:
        """ Функция отрисовки большого зерна
        :return: Null
        """
        source = pyray.Rectangle(0, 0, self.texture.width, self.texture.height)
        dest = pyray.Rectangle(self.rect.x + 14, self.rect.y + 14, self.texture.width, self.texture.height)
        origin = pyray.Vector2(self.rect.width // 2, self.rect.height // 2)
        pyray.draw_texture_pro(self.texture, source, dest, origin, self.rotation, pyray.WHITE)


class Cherry(Seed):
    filename = 'images/cherry.png'

    def __init__(self, game, rect: pyray.Rectangle) -> None:
        """ Класс вишенки, позволяющий работать с их отрисовкой и появлением
        :param game: все переменные игры
        :type game: Game
        :param rect: положение, длина и ширина
        :type rect: pyray.Rectangle
        """
        super().__init__(game, rect)
        self.texture = self.game.Textures.get_texture(self.filename)

    def draw(self) -> None:
        """ Функция отрисовки вишенки
        :return: Null
        """
        time_diff = datetime.datetime.now() - self.game.Settings.get_gamescene_run_timer()
        if time_diff.total_seconds() > 10:
            source = pyray.Rectangle(0, 0, self.texture.width, self.texture.height)
            dest = pyray.Rectangle(self.rect.x + 14, self.rect.y + 14, self.texture.width, self.texture.height)
            origin = pyray.Vector2(self.rect.width // 2, self.rect.height // 2)
            pyray.draw_texture_pro(self.texture, source, dest, origin, self.rotation, pyray.WHITE)
            if not self.game.Settings.get_bool_of_cherry_exsist():
                self.game.Settings.update_cherry_exsist()


class Gate(Empty):
    def __init__(self, game, rect: pyray.Rectangle) -> None:
        """ Класс "входа в комнату призраков" на игровой сцене, позволяющий работать с ним. Не имеет текстуры
        :param game: все переменные игры
        :type game: Game
        :param rect: положение, длина и ширина
        :type rect: pyray.Rectangle
        """
        super().__init__(game, rect)
        self.height_of_gate = 3

    def draw(self) -> None:
        """ Функция отрисовки входа в комнату призраков с высотой 3
        :return: Null
        """
        draw_rect = pyray.Rectangle(self.rect.x, self.rect.y, self.rect.width, self.height_of_gate)
        pyray.draw_rectangle_rec(draw_rect, colors.WHITE)

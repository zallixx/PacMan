import pyray

from objects.texture import Image

# Импортим класс(Image) для создания объектов из
# texture.py(.../objects/texture.py)
# Для получения большей информации о классе - перейдите в файл


class Cherry(Image):
    def __init__(self, game, texture: pyray.Texture, rect: pyray.Rectangle, weight: int) -> None:
        """ Класс вишенки, позволяющий работать с их отрисовкой и появлением
        :param game: все переменные игры
        :type game: Game
        :param texture: текстура
        :type texture: pyray.Texture
        :param rect: положение, длина и ширина
        :type rect: pyray.Rectangle
        :param weight: вес вишенки
        :type weight: int
        """
        super().__init__(game, texture, rect)
        self.weight = weight
        self.eaten = False
        self.radius = 0
        self.coordinate = [rect.x, rect.y]

    def show(self) -> None:
        """ Функция, назначающая радиус вишенки, то есть 12
        :return: Null
        """
        self.radius = 12

    def hide(self) -> None:
        self.radius = 0
        """ Функция, которая прячет вишенку
        :return: Null
        """

        # TODO: Не думаю, что данный класс должен выглядеть так. Во-первых появление вишенки надо бы сделать через также, как у seed(energizer). А удаление вишенки - съеданием пакмана
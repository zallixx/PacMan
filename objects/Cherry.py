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
        """ Функция, отвечабющая за появление вишенки. Работает посредством назначения нового радиуса вишенки
        :return: Null
        """
        self.radius = 12

    def hide(self) -> None:
        """ Функция, отвечающая за пропажу вишенки. Работает посредством назначения нового радиуса вишенки
         :return: Null
         """
        self.radius = 0

        # TODO: Не думаю, что данный класс должен выглядеть так.
        #  TODO: Во-первых появление вишенки надо бы сделать через также, как у seed(energizer).
        #   TODO: А удаление вишенки - съеданием пакмана

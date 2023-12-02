import pyray

from objects.Sprite import Sprite

#  Пара переменных и draw_texture_pro данного класса взяты из лекции(15.11.2023), которую проводил Кучук Егор Андреевич.
#  Выражаем огромную благодарность Егору Андреевичу!


class Textures:
    def __init__(self) -> None:
        """ Класс текстур, содержит словарь текстур
            self.list_textures имеет стуктуру "path_to_image": pyray.Texture
        """
        self.list_textures = {}

    def load_and_get_image(self, path: str) -> pyray.Texture:
        """ Загрузка и получение текстуры
        :param path: путь до картинки
        :type path: str
        :rtype: pyray.Texture
        :return: возвращает текстуру для объекта
        """
        if path not in self.list_textures:
            pic = pyray.load_image(path)
            texture = pyray.load_texture_from_image(pic)
            pyray.unload_image(pic)
            self.list_textures[path] = texture
            return texture
        else:
            print("Текстура уже загружена!")

    def unload_image(self, path: str) -> None:
        """ Выгрузка(удаление) текстуры
        :param path: путь до картинки
        :type path: str
        :return: Null
        """
        if path in self.list_textures:
            del self.list_textures[path]
        print("Данной текстуры нет")

    def get_texture(self, path: str) -> pyray.Texture:
        """ Получение текстуры
        :param path: путь до картинки
        :type path: str
        :rtype: pyray.Texture
        :return: возвращает текстуру для объекта
        """
        if path in self.list_textures:
            return self.list_textures[path]
        print("Ошибка при получении текстуры")

    def load_main_textures(self) -> None:
        """ Загрузка базовых текстур, которые используются при отрисовки игрового поля
        :return: Null
        """
        main_textures_path = ["images/seed.png", "images/bigseed.png", "images/pacmanup.png",
                              "images/orangeghostup.png", "images/pinkghostdown.png", "images/cyanghostup.png",
                              "images/redghostleft.png", "images/pacmandown.png", "images/pacmanleft.png",
                              "images/pacmanright.png", "images/cherry.png"]
        for path in main_textures_path:
            if path not in self.list_textures:
                pic = pyray.load_image(path)
                texture = pyray.load_texture_from_image(pic)
                pyray.unload_image(pic)
                self.list_textures[path] = texture

    def clear_textures(self) -> None:
        """ Очистка текстур(пока пустая)
        :return: Null
        """
        pass


class Image(Sprite):
    def __init__(self, game, texture: pyray.Texture, rect: pyray.Rectangle) -> None:
        """ Класс картинки, содержит отрисовку картинки, а также методы, наследуемые от родительскоого класса(Sprite)
        :param game: все переменные игры
        :type game: Game
        :param texture: текстура
        :type texture: pyray.Texture
        :param rect: положение, длина и ширина
        :type rect: pyray.Rectangle
        """
        super().__init__(game)
        self.rect = rect
        self.texture = texture
        self.rotation = 0

    def draw(self) -> None:
        """ Отрисовка текстуры
        :return: Null
        """
        if self.texture:
            source = pyray.Rectangle(0, 0, self.texture.width, self.texture.height)
            dest = pyray.Rectangle(self.rect.x, self.rect.y, self.rect.width, self.rect.height)
            origin = pyray.Vector2(self.rect.width // 2, self.rect.height // 2)
            pyray.draw_texture_pro(self.texture, source, dest, origin, self.rotation, pyray.WHITE)

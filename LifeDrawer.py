import pyray
from raylib import colors
from objects.texture import Image


class LifeDrawer(Image):
    def __init__(self, rect: pyray.Rectangle, texture: pyray.Texture, game, lifecount=3) -> None:
        """ Класс отрисовки жизней пакмана, который позволяет работать с их отрисовкой и удалением
        :param rect: координаты для отрисовки жизней
        :type rect: pyray.Rectangle
        :param lifecount: кол-во жизней
        :type lifecount: int
        """
        super().__init__(game, texture, rect)
        self.lifecount = lifecount
        self.game = game
        self.texture = texture
        size_of_texture = self.game.Settings.get_width_and_height_of_lifes()
        self.texture.width = size_of_texture[0]
        self.texture.height = size_of_texture[1]

    def draw(self) -> None:
        """ Функция отрисовки жизней
        :return: Null
        """
        for i in range(self.lifecount):
            pyray.draw_texture(self.texture, int(self.rect.x) + (i * 42), int(self.rect.y), colors.YELLOW)

    # будет вызываться по нажатию на клавишу F
    def remove(self) -> None:
        """ Функция убавления жизней у пакмана
        :return: Null
        """
        self.lifecount -= 1

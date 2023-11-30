import pyray
from raylib import colors
from objects.Sprite import Sprite


class LifeDrawer(Sprite):
    def __init__(self, rect: pyray.Rectangle, lifecount=3) -> None:
        """ Класс отрисовки жизней пакмана, который позволяет работать с их отрисовкой и удалением
        :param rect: координаты для отрисовки жизней
        :type rect: pyray.Rectangle
        :param lifecount: кол-во жизней
        :type lifecount: int
        """
        self.lifecount = lifecount
        self.radius = 14
        self.coordinate = [rect.x, rect.y]

    def draw(self) -> None:
        """ Функция отрисовки жизней
        :return: Null
        """
        for i in range(self.lifecount):
            pyray.draw_circle(int(self.coordinate[0]) + (i * 3 * self.radius), int(self.coordinate[1]), self.radius,
                              colors.YELLOW)

    # будет вызываться по нажатию на клавишу F
    def remove(self) -> None:
        """ Функция убавления жизней у пакмана
        :return: Null
        """
        self.lifecount -= 1

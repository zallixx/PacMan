import pyray
from raylib import colors
from Game_objects.Classes_of_objects_on_gamescene.Sprite import Sprite


class LifeDrawer(Sprite):
    def __init__(self, rect: pyray.Rectangle, lifecount=3, ) -> None:
        self.lifecount = lifecount
        self.radius = 14
        self.coordinate = [rect.x, rect.y]

    def draw(self):
        for i in range(self.lifecount):
            pyray.draw_circle(int(self.coordinate[0]) + (i * 3 * self.radius), int(self.coordinate[1]), self.radius,
                              colors.YELLOW)

    # будет вызываться по нажатию на клавишу F
    def remove(self):
        self.lifecount -= 1

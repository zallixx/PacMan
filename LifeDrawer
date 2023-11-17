import pyray
from raylib import colors
from pacman_developer.Game_objects.Objects_on_scene.Base_file_for_objects import Create_Object

class LifeDrawer(Create_Object):
    def __init__(self, path: str, rect: pyray.Rectangle, lifecount = 3,) -> None:
        super().__init__(path, rect)
        self.lifecount = lifecount
        self.radius = 14
        self.coordinate = [rect.x, rect.y]
    def draw(self):
        for i in range(self.lifecount):
            pyray.draw_circle(int(self.coordinate[0]) + (i*3*self.radius), int(self.coordinate[1]), self.radius, colors.YELLOW)
    # будет вызываться по нажатию на клавишу F
    def remove(self):
        self.lifecount -= 1

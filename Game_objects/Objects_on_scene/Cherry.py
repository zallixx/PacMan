import pyray
from raylib import colors
from Game_objects.Objects_on_scene.Base_file_for_objects import Create_Object

class Cherry(Create_Object):
    def __init__(self, path: str, rect: pyray.Rectangle, weight: int) -> None:
        super().__init__(path, rect)
        self.weight = weight
        self.eaten = False
        self.radius = 0
        self.coordinate = [rect.x, rect.y]
    def show(self):
        self.radius = 12
    def hide(self):
        self.radius = 0

from Game_objects.Objects_on_scene.Base_file_for_objects import Create_Object
import pyray

# Импортим класс для создания объектов из
# Base_file_for_objects.py(pacman_developer/Game_objects/Objects_on_scene)
# Для получения большей информации о классе - перейдите в файл


class Pacman(Create_Object):
    def __init__(self, path: str, rect: pyray.Rectangle) -> None:
        super().__init__(path, rect)

    def event(self) -> None:  # Описывается движение пакмана
        key_w = pyray.KeyboardKey.KEY_W
        key_a = pyray.KeyboardKey.KEY_A
        key_s = pyray.KeyboardKey.KEY_S
        key_d = pyray.KeyboardKey.KEY_D
        if pyray.is_key_down(key_w):
            self.coordinate[1] -= 1
        if pyray.is_key_down(key_s):
            self.coordinate[1] += 1
        if pyray.is_key_down(key_a):
            self.coordinate[0] -= 1
        if pyray.is_key_down(key_d):
            self.coordinate[0] += 1

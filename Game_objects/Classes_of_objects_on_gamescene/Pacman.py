from Game_objects.Classes_of_objects_on_gamescene.Base_file_for_objects import Create_Object
import pyray


# Импортим класс для создания объектов из
# Base_file_for_objects.py(pacman_developer/Game_objects/Classes_of_objects_on_gamescene)
# Для получения большей информации о классе - перейдите в файл


class Pacman(Create_Object):
    def __init__(self, path: str, rect: pyray.Rectangle, game) -> None:
        super().__init__(path, rect)
        self.game = game

    def event(self) -> None:
        key_w = pyray.KeyboardKey.KEY_W
        key_a = pyray.KeyboardKey.KEY_A
        key_s = pyray.KeyboardKey.KEY_S
        key_d = pyray.KeyboardKey.KEY_D
        if pyray.is_key_down(key_w):
            self.coordinate[1] -= 1
        if pyray.is_key_down(key_s):
            self.coordinate[1] += 1
        if pyray.is_key_down(key_a):
            if self.coordinate[0] > 156:
                self.coordinate[0] -= 1
        if pyray.is_key_down(key_d):
            if self.coordinate[0] < 646:
                self.coordinate[0] += 1
        list_of_teleports = self.game.current_scene.draw_field.list_of_teleport
        for i in range(len(list_of_teleports)):
            teleport_rect = pyray.Rectangle(list_of_teleports[i][0], list_of_teleports[i][1],
                                            list_of_teleports[i][2],
                                            list_of_teleports[i][3])
            pacman_rect = pyray.Rectangle(self.coordinate[0] - self.width / 2,
                                          self.coordinate[1] - self.height / 2, self.width,
                                          self.height)

            if pyray.check_collision_recs(teleport_rect, pacman_rect):
                if i == 0:
                    self.coordinate = [634 - 36, 272]
                else:
                    self.coordinate = [148 + 36, 272]

        # TODO: В классе Pacman нужно начать работу над телепортами и кушанием всякой всячины

    def logic(self) -> None:
        walls_rectangles = self.game.current_scene.draw_field.list_of_walls_rectangles
        for i in range(0,
                       len(walls_rectangles)):  # Цикл по pyray.Rectangle в списке walls_rectangles который создается в Cell_class.py
            cube_rect = pyray.Rectangle(walls_rectangles[i][0], walls_rectangles[i][1], walls_rectangles[i][2],
                                        walls_rectangles[i][
                                            3])  # Создание pyray.Rectangle на основе x, y, self.s, self.s(self.s = 18)
            pacman_rect = pyray.Rectangle(self.coordinate[0] - self.width / 2,
                                          self.coordinate[1] - self.height / 2, self.width,
                                          self.height)  # Создание pyray.Rectangle на основе x(пакмана), y(пакмана),
            # self.pacman.width(18), self.pacman.height(18)

            if pyray.check_collision_recs(cube_rect, pacman_rect):
                overlap_x = min(pacman_rect.x + pacman_rect.width, cube_rect.x + cube_rect.width) - max(pacman_rect.x,
                                                                                                        cube_rect.x)
                overlap_y = min(pacman_rect.y + pacman_rect.height, cube_rect.y + cube_rect.height) - max(pacman_rect.y,
                                                                                                          cube_rect.y)
                # Эти две переменные представляют собой размер области,
                # где прямоугольники пересекаются по горизонтали и вертикали соответственно

                if overlap_x < overlap_y:
                    # Если перекрытие по оси x меньше, чем по оси y, значит коллизия произошла горизонтально
                    if pacman_rect.x < cube_rect.x:  # Проверка на центр пакмана и центр блока по y
                        # Cмещаем пакмана влево
                        self.coordinate[0] -= overlap_x
                    else:
                        # Cмещаем пакмана вправо
                        self.coordinate[0] += overlap_x
                else:
                    # Коллизия произошла вертикально
                    if pacman_rect.y < cube_rect.y:  # Проверка на центр пакмана и центр блока по y
                        # Смещаем пакмана вверх
                        self.coordinate[1] -= overlap_y
                    else:
                        # Cмещаем пакмана вниз
                        self.coordinate[1] += overlap_y

from Game_objects.Classes_of_objects_on_gamescene.Sprite import Sprite
import pyray


# Импортим класс для создания объектов из
# Sprite.py(pacman_developer/Game_objects/Classes_of_objects_on_gamescene)
# Для получения большей информации о классе - перейдите в файл


class Pacman(Sprite):
    def __init__(self, path: str, rect: pyray.Rectangle) -> None:
        super().__init__(path, rect)
        self.textures = {"UP": pyray.load_texture("images/sprites/pacmanup.png"),
                         "DOWN": pyray.load_texture("images/sprites/pacmandown.png"),
                         "LEFT": pyray.load_texture("images/sprites/pacmanleft.png"),
                         "RIGHT": pyray.load_texture("images/sprites/pacmanright.png")}

    def event(self, list_of_teleports: list, list_of_seeds: list,
              list_of_energizer: list) -> None:  # Описывается движение пакмана
        if pyray.is_key_down(pyray.KeyboardKey.KEY_W):
            self.coordinate[1] -= 1
            self.texture=self.textures["UP"]
        if pyray.is_key_down(pyray.KeyboardKey.KEY_S):
            self.coordinate[1] += 1
            self.texture=self.textures["DOWN"]
        if pyray.is_key_down(pyray.KeyboardKey.KEY_A):
            self.coordinate[0] -= 1
            self.texture=self.textures["LEFT"]
        if pyray.is_key_down(pyray.KeyboardKey.KEY_D):
            self.coordinate[0] += 1
            self.texture=self.textures["RIGHT"]

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

    def logic(self, walls_rectangles: list) -> None:
        # Да.. данная функция крайне не понятна. Что ж, постараюсь объяснить

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

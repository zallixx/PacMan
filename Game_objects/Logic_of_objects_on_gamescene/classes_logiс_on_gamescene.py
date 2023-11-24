import pyray

from Game_objects.Classes_of_objects_on_gamescene.Pacman import Pacman
from Game_objects.Classes_of_objects_on_gamescene.Ghost import Ghost


class logic_of_pacman:
    def __init__(self) -> None:
        self.pacman = Pacman("frog.png", pyray.Rectangle(400, 335, 18, 18))
        self.teleport_timer = 0
        # Создаем self.pacman на основе класса Pacman
        # TODO: Текстуры

    def draw(self) -> None:
        self.pacman.draw()
        # Отрисовка пакмана
        # Написана так, потому что logic_of_pacman не имеет собственной отрисовки, в отличие от класса пакмана

    def event(self, list_of_teleports: list, list_of_seeds: list, list_of_energizer: list) -> None:
        self.pacman.event()  # Передвижение пакмана

        for i in range(len(list_of_teleports)):
            teleport_rect = pyray.Rectangle(list_of_teleports[i][0], list_of_teleports[i][1], list_of_teleports[i][2],
                                            list_of_teleports[i][3])
            pacman_rect = pyray.Rectangle(self.pacman.coordinate[0] - self.pacman.width / 2,
                                          self.pacman.coordinate[1] - self.pacman.height / 2, self.pacman.width,
                                          self.pacman.height)

            if pyray.check_collision_recs(teleport_rect, pacman_rect):
                if self.teleport_timer <= 0:
                    if i == 0:
                        self.pacman.coordinate = [634, 272]
                    else:
                        self.pacman.coordinate = [148, 272]
                    self.teleport_timer = 10
                else:
                    self.teleport_timer -= pyray.get_frame_time()


        # TODO: В классе Pacman нужно начать работу над телепортами и кушанием всякой всячины

    def logic(self, walls_rectangles: list) -> None:
        # Да.. данная функция крайне не понятна. Что ж, постараюсь объяснить
        for i in range(0,
                       len(walls_rectangles)):  # Цикл по pyray.Rectangle в списке walls_rectangles который создается в Cell_class.py
            cube_rect = pyray.Rectangle(walls_rectangles[i][0], walls_rectangles[i][1], walls_rectangles[i][2],
                                        walls_rectangles[i][
                                            3])  # Создание pyray.Rectangle на основе x, y, self.s, self.s(self.s = 18)
            pacman_rect = pyray.Rectangle(self.pacman.coordinate[0] - self.pacman.width / 2,
                                          self.pacman.coordinate[1] - self.pacman.height / 2, self.pacman.width,
                                          self.pacman.height)  # Создание pyray.Rectangle на основе x(пакмана), y(пакмана),
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
                        self.pacman.coordinate[0] -= overlap_x
                    else:
                        # Cмещаем пакмана вправо
                        self.pacman.coordinate[0] += overlap_x
                else:
                    # Коллизия произошла вертикально
                    if pacman_rect.y < cube_rect.y:  # Проверка на центр пакмана и центр блока по y
                        # Смещаем пакмана вверх
                        self.pacman.coordinate[1] -= overlap_y
                    else:
                        # Cмещаем пакмана вниз
                        self.pacman.coordinate[1] += overlap_y

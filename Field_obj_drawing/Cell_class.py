import pyray
from raylib import colors
from pacman_developer.Game_objects.Classes_of_objects_on_gamescene.Seed_and_Energizer import Seed, Energizer


class Cell:
    def __init__(self, size: int) -> None:  # На вход подаешся размер стороны ячейки
        self.s = size
        self.seed = Seed("frog.png", pyray.Rectangle(0, 0, self.s-10, self.s-10), 10)
        # Временное решение - frog.png. TODO: Текстуры
        self.energizer = Energizer("frog.png", pyray.Rectangle(0, 0, self.s-5, self.s-5), 10)
        self.list_of_walls_rectangles = []  # Список с координатами стены и её размером

    def draw_cell(self, cell: str, x: int, y: int) -> None:
        match cell:
            case 0:  # Пустота
                pass
            case 1:  # Прорисовка стены
                pyray.draw_rectangle(x, y, self.s, self.s, colors.BLUE)

                if [x, y, self.s, self.s] not in self.list_of_walls_rectangles:
                    # Проверка, есть ли [x, y, self.s, self.s] стены в list_of_walls_rectangles
                    self.list_of_walls_rectangles.append([x, y, self.s, self.s])

            case 2:  # Прорисовка телепорта
                pyray.draw_rectangle(x, y, self.s, self.s, colors.DARKPURPLE)
            case 3:  # Зерно
                self.seed.coordinate = [x+10, y+10]
                self.seed.draw()
            case 4:  # Большое зерно
                self.energizer.coordinate = [x+10, y+10]
                self.energizer.draw()
            case _:
                pass

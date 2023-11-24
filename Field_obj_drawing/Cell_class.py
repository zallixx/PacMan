import pyray
from raylib import colors
from pacman_developer.Game_objects.Classes_of_objects_on_gamescene.Seed_and_Energizer import Seed, Energizer


class Cell:
    def __init__(self, size):  # На вход подаешся размер стороны ячейки
        self.s = size
        self.seed = Seed("frog.png", pyray.Rectangle(0, 0, self.s-5, self.s-5), 10)
        # Временное решение - frog.png. TODO: Текстуры
        self.energizer = Energizer("frog.png", pyray.Rectangle(0, 0, self.s, self.s), 10)

    def draw_cell(self, cell: str, x: int, y: int):
        match cell:
            case 0:  # Пустота
                pass
            case 1:  # Прорисовка стены
                pyray.draw_rectangle(x, y, self.s, self.s, colors.BLUE)
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

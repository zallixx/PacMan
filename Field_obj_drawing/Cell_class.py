import pyray
from raylib import colors
from Game_objects.Objects_on_scene.Seed_and_Energizer import Seed, Energizer


class Cell:
    def __init__(self, size):  # На вход подаешся размер стороны ячейки
        self.s = size

    def draw_cell(self, cell: str, x: int, y: int):
        match cell:
            case 0:  # Пустота
                pass
            case 1:  # Прорисовка стены
                pyray.draw_rectangle(x, y, self.s, self.s, colors.BLUE)
            case 2:  # Прорисовка телепорта
                pyray.draw_rectangle(x, y, self.s, self.s, colors.DARKPURPLE)
            case 3:  # Зерно
                d = Seed("frog.png", pyray.Rectangle(x, y, self.s, self.s), 10)
                d.draw()
            case 4:  # Большое зерно
                d1 = Energizer("frog.png", pyray.Rectangle(x, y, self.s, self.s), 10)
                d1.draw()

import pyray
from raylib import colors


class Cell:
    def __init__(self, sizex: int, sizey: int):
        self.sx = sizex
        self.sy = sizey

    def draw_cell(self, cell: str, x: int, y: int):
        match cell:
            case 0:
                pass
            case 1:  # Прорисовка стены
                pyray.draw_rectangle(x, y, self.sx, self.sy, colors.BLUE)
            case 2:  # Прорисовка телепорта
                pyray.draw_rectangle(x, y, self.sx, self.sy, colors.DARKPURPLE)
            case 3:  # Зерно
                pass
            case 4:  # Большое зерно
                pass
            case _:
                pass

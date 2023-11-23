import pyray
from raylib import colors


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
                pass
            case 4:  # Большое зерно
                pass
            case _:
                pass

        #  Зёрна пока что не отрисовываются, но по факту они есть в самом массиве поля,
        #  так что с ними уже можно взаимодействовать.

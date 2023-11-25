import pyray
from raylib import colors
from objects.Seed_and_Energizer import Seed, Energizer


class Cell:
    def __init__(self, size: int, game) -> None:  # На вход подаешся размер стороны ячейки
        self.s = size
        self.game = game
        self.game.Textures.clear_textures()
        self.game.Textures.load_main_textures()
        self.seed = Seed(self.game.Textures.get_texture("images/seed.png"), pyray.Rectangle(0, 0, self.s-12, self.s-12), 10)
        self.energizer = Energizer(self.game.Textures.get_texture("images/bigseed.png"), pyray.Rectangle(0, 0, self.s-5, self.s-5), 15)
        self.list_of_walls_rectangles = []  # Список с координатами стены и её размером
        self.list_of_teleport = []
        self.list_of_seeds = []
        self.list_of_energizer = []

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

                if [x, y, self.s, self.s] not in self.list_of_teleport:
                    # Проверка, есть ли [x, y, self.s, self.s] телепорта в list_of_teleport
                    self.list_of_teleport.append([x, y, self.s, self.s])

            case 3:  # Зерно
                self.seed.coordinate = [x+9, y+9]
                self.seed.draw()

                if [x+10, y+10, self.s, self.s] not in self.list_of_seeds:
                    # Проверка, есть ли [x, y, self.s, self.s] зерна в list_of_seeds
                    self.list_of_seeds.append([x+10, y+10, self.s, self.s])

            case 4:  # Большое зерно
                self.energizer.coordinate = [x+9, y+9]
                self.energizer.draw()

                if [x+10, y+10, self.s, self.s] not in self.list_of_energizer:
                    # Проверка, есть ли [x, y, self.s, self.s] большого зерна в list_of_energizer
                    self.list_of_energizer.append([x+9, y+9, self.s, self.s])
            case _:
                pass
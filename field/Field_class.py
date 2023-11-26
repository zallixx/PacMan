import pyray

from objects.cells import Wall, Empty, Teleport, Seed, BigSeed, Gate
from objects.texture import Image


class Field(Image):  # В класс передаётся путь txt файла с полем
    CELL_SIZE = 18

    def __init__(self, game, x: int, y: int):
        """ Поле для игры пакман
        :param game: все переменные игры
        :type game: Game
        :param x: положение поля по x
        :type x: int
        :param y: положение поля по y
        :type y: int
        """
        super().__init__(game, None, pyray.Rectangle(x, y, (x + (28 * Field.CELL_SIZE)), (y + (31 * Field.CELL_SIZE))))
        self.field_path = 'field/field.txt'
        self.field_data = []
        self.load(self.field_path)

    def load(self, field_path: str) -> None:
        """ Загрузка поля в переменную field_data
        :param field_path: путь до поля
        :type field_path: str
        :return: Null
        """
        with open(field_path) as file:
            self.field_data = self.convert(
                [s.strip('\n') for s in file.readlines()]
            )

    @staticmethod
    def convert_str_to_tile(value: int):
        """Преобразовывает строчное значение в класс клетки
        :param value: значение клетки
        :type value: int
        :return: класс клетки
        """
        tiles = {
            "#": Wall,
            "_": Empty,
            "T": Teleport,
            ".": Seed,
            "S": BigSeed,
            "+": Gate
        }
        try:
            return tiles[value]
        except KeyError:
            raise RuntimeError("Это что за клетка вообще?")

    def get_field(self):
        """ Возвращает всё поле в виде двумерного массива
        :rtype list[row][col]:
        :return: поле в виде двумерного массива
        """
        return self.field_data

    def convert(self, lines: list):
        """ Заполняет массив field классами клеток
        :param lines: линии для преобразования
        :type lines: list
        :rtype list[row][col]:
        :return: поле в виде двумерного массива
        """
        field_data = []
        for i, line in enumerate(lines):
            row = []
            for j, value in enumerate(line):
                tile_type = self.convert_str_to_tile(value)
                tile = tile_type(
                    self.game,
                    pyray.Rectangle(self.rect.x + j * Field.CELL_SIZE, self.rect.y + i * Field.CELL_SIZE,
                                    Field.CELL_SIZE, Field.CELL_SIZE)
                )
                row.append(tile)
            field_data.append(row)
        return field_data

    def draw(self) -> None:
        """Отрисовка каждой клетки
        :return: Null
        """
        for row in self.field_data:
            for tile in row:
                tile.draw()

    def get_tile(self, row: int, col: int):
        """ Получение клетки по строке и столбцу
        :param row: строка
        :type row: int
        :param col: столбец
        :type col: int
        :return: клетка
        """
        return self.field_data[row][col]

    def get_tile_by_coords(self, x: int, y: int) -> None:
        """Получение клетки по координатам
        :param x: координата x
        :type x: int
        :param y: координата y
        :type y: int
        :return:
        """
        row, col = self.coords_to_clear(x, y)
        return self.get_tile(row, col)

    def set_tile(self, tile, row: int, col: int) -> None:
        """Установить клетку по строке и столбцу
        :param tile: клетка
        :param row: строка
        :type row: int
        :param col: столбец
        :type col: int
        :return: Null
        """
        self.field_data[row][col] = tile

    def set_tile_by_coords(self, tile) -> None:
        """Установить клетку по координатам(достаются из клетки)
        :param tile: клетка
        :return: Null
        """
        row, col = self.coords_to_clear(tile.rect.x, tile.rect.y)
        self.set_tile(tile, row, col)

    def coords_to_clear(self, x: int, y: int) -> None:
        """Преобразовать координаты в строку и столбец
        :param x: координата x
        :type x: int
        :param y: координата y
        :type y:  int
        :rtype (int, int):
        :return: столбец и строка
        """
        col = (x - self.rect.x) // Field.CELL_SIZE
        row = (y - self.rect.y) // Field.CELL_SIZE
        return int(row), int(col)

import pyray

from objects.cells import Wall, Empty, Teleport, Seed, BigSeed
from objects.texture import Image


class Field(Image):  # В класс передаётся путь txt файла с полем
    CELL_SIZE = 18

    def __init__(self, game, x, y):
        super().__init__(game, None, pyray.Rectangle(x, y, (x + (28 * Field.CELL_SIZE)), (y + (31 * Field.CELL_SIZE))))
        self.field_path = 'field/field.txt'
        self.field_data = []
        self.load(self.field_path)

    def load(self, field_path):
        with open(field_path) as file:
            self.field_data = self.convert(
                [s.strip('\n') for s in file.readlines()]
            )

    @staticmethod
    def convert_str_to_tile(value):
        tiles = {
            "#": Wall,
            "_": Empty,
            "T": Teleport,
            ".": Seed,
            "S": BigSeed
        }
        try:
            return tiles[value]
        except KeyError:
            raise RuntimeError("Это что за клетка вообще?")

    def get_field(self):  # Возвращает всё поле в виде двумерного массива
        return self.field_data

    def convert(self, lines):
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

    def draw(self):
        for row in self.field_data:
            for tile in row:
                tile.draw()

    def get_tile(self, row, col):
        return self.field_data[row][col]

    def get_tile_by_coords(self, x, y):
        row, col = self.coords_to_clear(x, y)
        return self.get_tile(row, col)

    def set_tile(self, tile, row, col):
        self.field_data[row][col] = tile

    def set_tile_by_coords(self, tile, x, y):
        row, col = self.coords_to_clear(x, y)
        self.set_tile(tile, row, col)

    def coords_to_clear(self, x, y):
        col = (x - self.rect.x) // Field.CELL_SIZE
        row = (y - self.rect.y) // Field.CELL_SIZE
        return int(row), int(col)

from Field_obj_drawing.Field_class import Field
from Field_obj_drawing.Cell_class import Cell


class FieldDrawer:
    def __init__(self):
        self.x = 148  # Центрирование по длине ((длина окна - размер ячейки * кол-во рядов) / 2)
        self.y = 20
        self.field = Field("Field_obj_drawing/field.txt")
        self.field_data = self.field.get_field()
        self.cell = Cell(18)
        self.list_of_walls_rectangles = self.cell.list_of_walls_rectangles
        self.list_of_seeds = self.cell.list_of_seeds
        self.list_of_energizer = self.cell.list_of_energizer
        self.list_of_teleport = self.cell.list_of_teleport

    def draw_field(self):
        x = 148  # Центрирование по длине ((длина окна - размер ячейки * кол-во рядов) / 2)
        y = 20
        for i, row in enumerate(self.field_data):  # Перебор ячеек и их отрисовка
            for j, element in enumerate(row):
                self.cell.draw_cell(self.field_data[i][j], x, y)
                x += 18
            x = 148
            y += 18

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
        col = abs(x - self.x) // 18
        row = (y - self.y) // 18
        print(col, row)
        return int(row), int(col)

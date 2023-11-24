from Field_obj_drawing.Field_class import Field
from Field_obj_drawing.Cell_class import Cell


class FieldDrawer:
    def __init__(self):
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

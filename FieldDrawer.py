from Field_class import Field
from Cell_class import Cell


class FieldDrawer:
    def __init__(self, sizex: int = 18, sizey: int = 18):
        self.field = Field('field.txt')
        self.field_data = Field.get_field()
        self.cell = Cell(sizex, sizey)

    def draw_field(self):
        x = 19
        y = 9
        for i, row in enumerate(self.field_data):
            for j, element in enumerate(row):
                self.cell.draw_cell(self.field_data[i][j], x, y)
                x += 9
            y += 9

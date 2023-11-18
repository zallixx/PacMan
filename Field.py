class Field:  # В класс передаётся путь txt файла с полем

    def __init__(self, field_path: str):
        self.field_path = field_path
        self.field_data = []
        self._read_file()

    def _read_file(self):
        try:
            with open(self.field_path, 'r') as file:
                lines = file.readlines()
                self.field_data = [list(line.strip()) for line in lines]
        except FileNotFoundError:
            print(f"File '{self.field_path}' not found.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def get_field(self):  # Возвращает всё поле в виде двумерного массива
        return self.field_data

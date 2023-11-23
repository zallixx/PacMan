class Field:  # В класс передаётся путь txt файла с полем

    def __init__(self, field_path: str):
        self.field_path = field_path
        self.field_data = []
        self._read_file()
        self._convert()

    def _read_file(self):
        try:
            with open(self.field_path, 'r') as file:
                lines = file.readlines()
                self.field_data = [list(line.strip()) for line in lines]
        except FileNotFoundError:
            print(f"File '{self.field_path}' not found.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def _convert(self):  # Конвертация массива поля из str в int
        for i, row in enumerate(self.field_data):
            for j, value in enumerate(row):
                match value:
                    case "_":  # Пустое место
                        self.field_data[i][j] = 0
                    case "#":  # Стена
                        self.field_data[i][j] = 1
                    case "T":  # Телепорт
                        self.field_data[i][j] = 2
                    case ".":  # Зерно
                        self.field_data[i][j] = 3
                    case "S":  # Energizer
                        self.field_data[i][j] = 4
                    case _:
                        # Обработка других значений, если необходимо
                        pass

    def get_field(self):  # Возвращает всё поле в виде двумерного массива
        while True:
            return self.field_data

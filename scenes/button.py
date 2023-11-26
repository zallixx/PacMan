import pyray


class Button:
    def __init__(self, x_coordinate_of_button: int, y_coordinate_of_button: int, button_text: str) -> None:
        self.x_coordinate_of_button = x_coordinate_of_button
        self.y_coordinate_of_button = y_coordinate_of_button
        self.width = 200
        self.height = 50
        self.fontSize = 20
        self.text_in_button = button_text
        self.color_of_button = pyray.WHITE
        self.color_text_in_button = pyray.BLACK

    def draw(self) -> None:
        # Отрисовка самой кнопки
        pyray.draw_rectangle(self.x_coordinate_of_button, self.y_coordinate_of_button,
                             self.width, self.height, self.color_of_button)

        # Находим центр кнопки используя начальную координату(x, y) и ширину(высоту) / 2 соотвественно
        centre_of_button_x = self.x_coordinate_of_button + self.width / 2
        centre_of_button_y = self.y_coordinate_of_button + self.height / 2

        length_text_in_button = len(self.text_in_button)  # Получаем длину текста

        # Находим центр текста по x и y с учетом длины текста и размера шрифта
        centre_of_text_x = (centre_of_button_x - (length_text_in_button * (self.fontSize / 2) / 2))
        centre_of_text_y = (centre_of_button_y - (self.fontSize / 2))

        pyray.draw_text(self.text_in_button, int(centre_of_text_x), int(centre_of_text_y),
                        self.fontSize, self.color_text_in_button)

    def is_mouse_on_button(self) -> bool:
        mouse_x, mouse_y = pyray.get_mouse_x(), pyray.get_mouse_y()
        return (self.x_coordinate_of_button <= mouse_x <= self.x_coordinate_of_button + self.width and
                self.y_coordinate_of_button <= mouse_y <= self.y_coordinate_of_button + self.height)

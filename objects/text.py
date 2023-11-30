import pyray


class Text:
    def __init__(self, text: str, coords_text_vector2: pyray.Vector2,
                 fontSize: int, color_of_text: pyray.Color) -> None:
        """ Класс текста, позволяющий работать с ним
        :param text: текст
        :type text: str
        :param coords_text_vector2: положение текста по оси x и по y
        :type coords_text_vector2: pyray.Vector2
        :param fontSize: размер шрифта
        :type fontSize: int
        :param color_of_text: цвет текста
        :type color_of_text: pyray.Color
        """
        self.coords_text_vector2 = coords_text_vector2
        self.color_of_text = color_of_text
        self.text = text
        self.fontSize = fontSize

    def draw_text(self) -> None:
        """ Функция отрисовки текста
        :return: Null
        """
        pyray.draw_text(self.text, int(self.coords_text_vector2.x),
                        int(self.coords_text_vector2.y), self.fontSize, self.color_of_text)

    def get_text(self) -> str:
        """ Функция получения текста
        :return: str
        """
        return self.text


class RecalculableText(Text):
    def __init__(self, text: str, coords_text_vector2: pyray.Vector2,
                 fontSize: int, color_of_text: pyray.Color) -> None:
        """ Класс текста, основоный на классе Text. Данный класс имеет дополнительную функцию recreate_text. Аналог .format
        :param text: текст
        :type text: str
        :param coords_text_vector2: положение текста по оси x и по y
        :type coords_text_vector2: pyray.Vector2
        :param fontSize: размер шрифта
        :type fontSize: int
        :param color_of_text: цвет текста
        :type color_of_text: pyray.Color
        """
        super().__init__(text, coords_text_vector2, fontSize, color_of_text)
        self.text_format = self.text

    def recreate_text(self, *args: str, **kwargs: str) -> None:
        """ Функция форматирования текста
        :param args: то, что надо заменить kwargs
        :type args: str
        :param kwargs: то, на что нужно заменить
        :type kwargs: str
        :return: Null
        """
        self.text = self.text_format.format(*args, **kwargs)

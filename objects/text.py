import pyray


class Text:
    def __init__(self, text: str, x: int, y: int,
                 fontSize: int, color_of_text: pyray.Color) -> None:
        self.coords_text_vector2 = pyray.Vector2(x, y)
        self.color_of_text = color_of_text
        self.text = text
        self.fontSize = fontSize

    def draw_text(self) -> None:
        pyray.draw_text(self.text, int(self.coords_text_vector2.x),
                        int(self.coords_text_vector2.y), self.fontSize, self.color_of_text)

    def get_text(self) -> str:
        return self.text


class RecalculableText(Text):
    def __init__(self, text: str, x: int, y: int,
                 fontSize: int, color_of_text: pyray.Color) -> None:
        super().__init__(text, x, y, fontSize, color_of_text)
        self.text_format = self.text

    def recreate_text(self, *args, **kwargs) -> None:
        self.text = self.text_format.format(*args, **kwargs)

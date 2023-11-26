import pyray
from HighScore.HighscoreTable import HighscoreTable


class HighscoreTableDrawer:
    def __init__(self) -> None:
        """Отрисовка таблицы рекордов
        """
        self.highscoreTable = HighscoreTable()

    def draw(self, posX: int, posY: int, fontSize: int = 24, color=pyray.BLACK):
        """Отрисовка таблицы рекордов
        :param posX: позиция по x
        :type posX: int
        :param posY: позиция по y
        :type posY: int
        :param fontSize: размер шрифта
        :type fontSize: int
        :param color: цвет
        :type color: Raylib.colors
        :return: Null
        """
        text = 'High score table\n'
        for i in self.highscoreTable.table:
            text += f"{i['name']} {i['score']}\n"
        pyray.draw_text(text, posX, posY, fontSize, color)

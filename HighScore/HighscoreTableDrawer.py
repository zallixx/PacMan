import pyray
from HighScore.HighscoreTable import HighscoreTable
from objects.text import Text


class HighscoreTableDrawer:
    def __init__(self) -> None:
        """Отрисовка таблицы рекордов
        """
        self.highscoreTable = HighscoreTable()

    def draw(self, posX: int, posY: int, fontSize: int = 24, color=pyray.BLACK) -> None:
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

        highscoretable_text_object = Text('High score table\n', posX, posY, fontSize, color)
        for i in self.highscoreTable.table:
            highscoretable_text_object.text += f"{i['name']} {i['score']}\n"
        highscoretable_text_object.draw_text()

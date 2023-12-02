import pyray
from HighScore.HighscoreTable import HighscoreTable
from objects.text import RecalculableText


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
        self.highscoreTable.filterTable()
        highscoretable_text_object = RecalculableText('High score table\n{}', pyray.Vector2(posX, posY), fontSize, color)
        highscore_text = ''
        for i in self.highscoreTable.table:
            highscore_text += f"{i['name']} {i['score']}\n"
            highscoretable_text_object.recreate_text(highscore_text, "{}")
        highscoretable_text_object.draw_text()

    def draw_max(self, posX: int, posY: int, fontSize: int = 24, color=pyray.BLACK) -> None:
        """Отрисовка максимального значения из таблицы рекордов
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
        # Находим максимальное значение в таблице
        max_score = max(i['score'] for i in self.highscoreTable.table)

        # Загрузка в файл таблицы и последующая её выгрузка(для лайв-обновления таблицы)
        self.highscoreTable.saveDataToFile()
        self.highscoreTable.loadDataFromFile()

        # Создаем объект текста
        max_score_text_object = RecalculableText('Max Score: \n{}', pyray.Vector2(posX, posY), fontSize, color)
        max_score_text_object.recreate_text(max_score, "{}")

        # Отображаем текст
        max_score_text_object.draw_text()
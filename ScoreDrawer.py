import pyray
from raylib import colors
from objects.text import RecalculableText


class ScoreDrawer:
    def __init__(self, score: int = 0) -> None:
        """ Класс отрисовки счета, позволяющий работать с его отрисовкой и изменением
        :param score: счёт(который отоброжается и изменяется при съедании зерён)
        :type score: int
        """
        self.score = score
        self.font_size_score = 50
        self.score_text_object = RecalculableText("{}", pyray.Vector2(10, 30), self.font_size_score, pyray.WHITE)

    def draw(self) -> None:
        """ Функция отрисовки счета. Включает в себя форматирование текста
        :return: Null
        """
        self.score_text_object.recreate_text(str(self.score), "{}")
        self.score_text_object.draw_text()

    def add(self, point: int) -> None:
        """ Функция добавлния очков к счету пакмана
        :param point: кол-во очков, которые следует добавить к счету
        :type point: int
        :return: Null
        """
        self.score += point

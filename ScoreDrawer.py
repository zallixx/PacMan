import pyray
from raylib import colors
from objects.text import RecalculableText


class ScoreDrawer:

    def __init__(self, score: int = 0) -> None:
        self.score = score
        self.font_size_score = 50
        self.score_text_object = RecalculableText("{}", 10, 30, self.font_size_score, pyray.WHITE)

    def draw(self):
        self.score_text_object.recreate_text(str(self.score), "{}")
        self.score_text_object.draw_text()

    def add(self, point: int):
        self.score += point

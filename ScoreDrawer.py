import pyray
from raylib import colors
from objects.text import Text


class ScoreDrawer:

    def __init__(self, score: int = 0) -> None:
        self.score = score
        self.font_size_score = 50
        self.score_text_object = Text(str(self.score), 10, 30, self.font_size_score, pyray.WHITE)

    def draw(self):
        self.score_text_object.text = str(self.score)
        self.score_text_object.draw_text()

    def add(self, point):
        self.score += point
        

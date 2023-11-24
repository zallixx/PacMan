import pyray
from raylib import colors


class ScoreDrawer:  # (RecalculableText):

    def __init__(self, score: int = 0) -> None:
        self.score = score
        self.font_size_score = 50

    def draw(self):
        pyray.draw_text(str(self.score), 10, 30, self.font_size_score, colors.WHITE)

    def ScoreChanges(self):
        #self.score будет изменяться при съедании семечек.
        pass


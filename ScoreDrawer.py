import pyray
from raylib import colors


class ScoreDrawer:  # (RecalculableText):

    def __init__(self, score: int = 0) -> None:
        self.score = score
        self.font_size_score = 75

    def draw(self):
        pyray.draw_text(str(ScoreDrawer.score), 50, 10, self.font_size_score, colors.BLACK)

    def ScoreChanges(self):
        #self.score будет изменяться при съедании семечек.
        pass


import pyray
from HighscoreTable import HighscoreTable


class HighscoreTableDrawer:
    def __init__(self) -> None:
        self.highscoreTable = HighscoreTable()

    def draw(self, posX: int, posY: int, fontSize: int = 24, color=pyray.BLACK):
        text = ''
        for i in self.highscoreTable.table:
            text += f"{i['name']} {i['score']}\n"
        pyray.draw_text(text, posX, posY, fontSize, color)

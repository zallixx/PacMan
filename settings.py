import pyray
from ScoreDrawer import ScoreDrawer
from HighScore.HighscoreTableDrawer import HighscoreTableDrawer
from LifeDrawer import LifeDrawer

class Settings:
    def __init__(self) -> None:
        self.__width_of_window = 800
        self.__height_of_window = 600
        self.__title_of_window = "Pacman Game"
        self.__volume = 1
        self.__volume_step = 1
        self.__highscore = HighscoreTableDrawer()
        self.__score_draw = ScoreDrawer()
        self.__score_draw.score = 0
        self.__player_name = None
        self.__life_draw = LifeDrawer(pyray.Rectangle(680, 30, 18, 18))

    def init_window(self) -> None:
        pyray.init_window(self.__width_of_window, self.__height_of_window, self.__title_of_window)

    def get_width_of_window(self) -> int:
        return self.__width_of_window

    def get_height_of_window(self) -> int:
        return self.__height_of_window

    def get_volume_level(self) -> float:
        return self.__volume

    def get_volume_step(self) -> float:
        return self.__volume_step

    def change_volume(self, new_volume: int) -> None:
        self.__volume = new_volume

    def get_new_player_name(self) -> None:
        num = max([int(t['name'][6:]) for t in self.__highscore.highscoreTable.table]) + 1
        self.__player_name = f"player{num}"

    def draw_highscore(self) -> None:
        self.__highscore.draw(325, 275, 18, pyray.WHITE)

    def add_new_score_to_table(self) -> None:
        self.__highscore.highscoreTable.add_score(self.__player_name, self.__score_draw.score)

    def save_highscore(self) -> None:
        self.__highscore.highscoreTable.saveDataToFile()

    def draw_score(self) -> None:
        self.__score_draw.draw()

    def add_points_to_score(self, amount: int) -> None:
        self.__score_draw.add(amount)

    def score_reset(self) -> None:
        self.__score_draw.score = 0

    def draw_pacman_lifes(self) -> None:
        self.__life_draw.draw()

    def get_pacman_lifes(self) -> int:
        return self.__life_draw.lifecount

    def remove_pacman_life(self) -> None:
        self.__life_draw.remove()

    def update_pacman_lifes(self) -> None:
        self.__life_draw.lifecount = 3

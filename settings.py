import datetime
import pyray
from ScoreDrawer import ScoreDrawer
from HighScore.HighscoreTableDrawer import HighscoreTableDrawer
from LifeDrawer import LifeDrawer


class Settings:
    def __init__(self, game) -> None:

        self.game = game

        self.__width_of_window = 800
        self.__height_of_window = 600
        self.__title_of_window = "Pacman Game"
        self.__volume = 1
        self.__volume_step = 1
        self.__highscore = HighscoreTableDrawer()
        self.__score_draw = ScoreDrawer()
        self.__score_draw.score = 0
        self.__player_name = None
        self.__life_draw = None
        self.__amount_of_seeds = 246
        self.__width_of_lifes = 32
        self.__height_of_lifes = 32
        self.__total_time_after_gamescene_run = None
        self.__is_any_cherry_on_scene = False

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

    def draw_max(self) -> None:
        self.__highscore.draw_max(10, 90, 24, pyray.WHITE)

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

    def init_pacman_lifes(self) -> None:
        self.__life_draw = LifeDrawer(pyray.Rectangle(680, 30, 50, 50), self.game.Textures.get_texture("images/pacmanleft.png"), self.game)

    def draw_pacman_lifes(self) -> None:
        self.__life_draw.draw()

    def get_pacman_lifes(self) -> int:
        return self.__life_draw.lifecount

    def remove_pacman_life(self) -> None:
        self.__life_draw.remove()

    def update_pacman_lifes(self) -> None:
        self.init_pacman_lifes()
        self.__life_draw.lifecount = 3

    def minus_one_seed(self) -> None:
        self.__amount_of_seeds -= 1

    def get_amount_of_seeds(self) -> int:
        return self.__amount_of_seeds

    def get_width_and_height_of_lifes(self) -> list:
        return [self.__width_of_lifes, self.__height_of_lifes]

    def update_gamescene_run_timer(self) -> None:
        self.__total_time_after_gamescene_run = datetime.datetime.now()

    def get_gamescene_run_timer(self) -> datetime.datetime.now():
        return self.__total_time_after_gamescene_run

    def get_bool_of_cherry_exsist(self) -> bool:
        return self.__is_any_cherry_on_scene

    def update_cherry_exsist(self) -> None:
        if self.__is_any_cherry_on_scene:
            self.__is_any_cherry_on_scene = False
        else:
            self.__is_any_cherry_on_scene = True

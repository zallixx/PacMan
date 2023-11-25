import pyray
from scenes.menuscene import MenuScene
from HighScore.HighscoreTableDrawer import HighscoreTableDrawer
from LifeDrawer import LifeDrawer
from ScoreDrawer import ScoreDrawer


class Game:
    def __init__(self) -> None:
        self.window_width = 800
        self.window_height = 600
        self.current_scene = MenuScene(self)
        self.highscore = HighscoreTableDrawer()
        num = max([int(t['name'][6:]) for t in self.highscore.highscoreTable.table]) + 1
        self.PLAYER_NAME = f"player{num}"
        self.score_draw = ScoreDrawer()
        self.life_draw = LifeDrawer(pyray.Rectangle(680, 30, 18, 18))
        self.volume_level = 50

    def change_scene(self, scene) -> None:
        self.current_scene = scene

    def run(self) -> None:
        pyray.init_window(self.window_width, self.window_height, "Pacman Game")
        pyray.init_audio_device()
        pyray.set_target_fps(120)

        while not pyray.window_should_close():
            self.current_scene.process_input()
            self.current_scene.update()
            pyray.begin_drawing()
            pyray.clear_background(pyray.BLACK)
            self.current_scene.draw()
            pyray.end_drawing()

        pyray.close_window()
        pyray.close_audio_device()

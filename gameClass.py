import pyray
from Drawing_scenes.menuscene import MenuScene
from HighScore.HighscoreTableDrawer import HighscoreTableDrawer
from ScoreDrawer import ScoreDrawer


class Game:
    def __init__(self):
        self.window_width = 800
        self.window_height = 600
        self.current_scene = MenuScene(self)
        self.PLAYER_NAME = 'dev'
        self.highscore = HighscoreTableDrawer()
        self.score_draw = ScoreDrawer()

    def change_scene(self, scene):
        self.current_scene = scene

    def run(self):
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

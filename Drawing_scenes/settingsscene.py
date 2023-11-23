import pyray
from Drawing_scenes.scene import Scene

class SettingsScene(Scene):
    def __init__(self, game):
        super().__init__()
        self.game = game

    def process_input(self):
        pass

    def update(self):
        pass

    def draw(self):
        # Отрисовка сцены настроек
        pyray.draw_text("Setting Scene", 10, 10, 20, pyray.BLACK)
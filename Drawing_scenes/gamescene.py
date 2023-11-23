import pyray
from pacman_developer.Drawing_scenes.scene import Scene
from pacman_developer.Field_obj_drawing.FieldDrawer import FieldDrawer
class GameScene(Scene):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.draw_field = FieldDrawer()

    def process_input(self):
        pass

    def update(self):
        pass

    def draw(self):
        pyray.draw_text("Game Scene", 10, 10, 20, pyray.BLACK)
        self.draw_field.draw_field()


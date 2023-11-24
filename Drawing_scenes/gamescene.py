import pyray
from Drawing_scenes.scene import Scene
from Field_obj_drawing.FieldDrawer import FieldDrawer
from pacman_developer.Game_objects.Logic_of_objects_on_gamescene.classes_login_on_gamescene import logic_of_pacman


class GameScene(Scene):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.draw_field = FieldDrawer()
        self.pacman_logic = logic_of_pacman()

    def process_input(self):
        pass

    def update(self):
        pass

    def draw(self):
        pyray.draw_text("Game Scene", 10, 10, 20, pyray.BLACK)
        self.draw_field.draw_field()
        self.pacman_logic.draw()
        self.pacman_logic.event()
        self.pacman_logic.logic()
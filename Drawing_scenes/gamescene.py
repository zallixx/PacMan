import pyray
from Drawing_scenes.scene import Scene
from Field_obj_drawing.FieldDrawer import FieldDrawer
from Game_objects.Classes_of_objects_on_gamescene.Pacman import Pacman
from Game_objects.audio import Audio
from pacman_developer.ScoreDrawer import ScoreDrawer

class GameScene(Scene):
    def __init__(self, game) -> None:
        super().__init__()
        self.game = game
        self.draw_field = FieldDrawer()
        self.score_draw = ScoreDrawer()
        self.pacman = Pacman("images/sprites/pacmanup.png", pyray.Rectangle(400, 335, 18, 18))
        self.start_audio = Audio(game)
        self.start_audio.play_track()
        # Создаем self.pacman на основе класса Pacman

    def process_input(self) -> None:
        from Drawing_scenes.pausescene import PauseScene
        if pyray.is_key_pressed(pyray.KeyboardKey.KEY_P):
            self.game.change_scene(PauseScene(self.game, self))

    def update(self) -> None:
        pass

    def draw(self) -> None:
        pyray.draw_text("Game Scene", 10, 10, 20, pyray.WHITE)  # Отрисовка текста Game Scene в левом верхнем углу

        self.draw_field.draw_field()  # Отрисовка поля
        self.pacman.draw()  # Отрисовка пакмана
        self.score_draw.draw()  # Отрисовка счета
        self.pacman.event(self.draw_field.list_of_teleport, self.draw_field.list_of_seeds,
                          self.draw_field.list_of_energizer)  # Передвижение пакмана
        self.pacman.logic(self.draw_field.list_of_walls_rectangles)  # Логика пакмана
        # TODO: Нужно сделать так, чтобы пакман мог есть..

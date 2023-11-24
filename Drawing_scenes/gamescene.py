import pyray
from Drawing_scenes.scene import Scene
from Field_obj_drawing.FieldDrawer import FieldDrawer
from Game_objects.Classes_of_objects_on_gamescene.Pacman import Pacman


class GameScene(Scene):
    def __init__(self, game) -> None:
        super().__init__()
        self.game = game
        self.draw_field = FieldDrawer()
        self.pacman = Pacman("images/frog.png", pyray.Rectangle(400, 335, 18, 18), game)
        # Создание pacman_logic на основе класса логики/передвижения пакмана на игровой сцене

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
        self.pacman.event()  # Передвижение пакмана
        self.pacman.logic()  # Логика пакмана
        # TODO: Нужно сделать так, чтобы пакман мог есть..

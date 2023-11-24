import pyray
from Drawing_scenes.scene import Scene
from Field_obj_drawing.FieldDrawer import FieldDrawer
from Game_objects.Logic_of_objects_on_gamescene.classes_logiс_on_gamescene import logic_of_pacman


class GameScene(Scene):
    def __init__(self, game) -> None:
        super().__init__()
        self.game = game
        self.draw_field = FieldDrawer()
        self.pacman_logic = logic_of_pacman()
        # Создание pacman_logic на основе класса логики/передвижения пакмана на игровой сцене

    def process_input(self) -> None:
        from Drawing_scenes.pausescene import PauseScene
        if pyray.is_key_pressed(pyray.KeyboardKey.KEY_P):
            self.game.change_scene(PauseScene(self.game))

    def update(self) -> None:
        pass

    def draw(self) -> None:
        pyray.draw_text("Game Scene", 10, 10, 20, pyray.BLACK)  # Отрисовка текста Game Scene в левом верхнем углу
        self.draw_field.draw_field()  # Отрисовка поля
        self.pacman_logic.draw()  # Отрисовка пакмана
        self.pacman_logic.event()  # Передвижение пакмана
        self.pacman_logic.logic(self.draw_field.list_of_walls_rectangles)  # Логика пакмана(колизия)
        # TODO: Нужно сделать так, чтобы пакман мог есть..

import pyray
from Drawing_scenes.scene import Scene
from Field_obj_drawing.FieldDrawer import FieldDrawer
from Game_objects.Classes_of_objects_on_gamescene.Pacman import Pacman
from Game_objects.Classes_of_objects_on_gamescene.Ghost import Ghost
from Game_objects.audio import Audio


class GameScene(Scene):
    def __init__(self, game) -> None:
        super().__init__()
        self.game = game
        self.draw_field = FieldDrawer()
        self.objects = [Pacman("images/sprites/pacmanup.png", pyray.Rectangle(409, 335, 18, 18), self.game),
                        Ghost("images/sprites/orangeghostup.png", pyray.Rectangle(445, 299, 18, 18), "y", 0, self.game),
                        Ghost("images/sprites/pinkghostdown.png", pyray.Rectangle(415, 299, 18, 18), "x", 0, self.game),
                        Ghost("images/sprites/cyanghostup.png", pyray.Rectangle(385, 299, 18, 18), "y", 0, self.game),
                        Ghost("images/sprites/redghostleft.png", pyray.Rectangle(355, 299, 18, 18), "x", 0, self.game)]
        self.start_audio = Audio(game, 0.4)
        self.start_audio.play_track()
        self.game.score_draw.score=0

    def process_input(self) -> None:
        from Drawing_scenes.pausescene import PauseScene
        if pyray.is_key_pressed(pyray.KeyboardKey.KEY_P):
            self.game.change_scene(PauseScene(self.game, self))
        if pyray.is_key_pressed(pyray.KeyboardKey.KEY_F):
            self.game.life_draw.remove()

    def update(self) -> None:
        pass

    def draw(self) -> None:
        pyray.draw_text("Game Scene", 10, 10, 20, pyray.WHITE)  # Отрисовка текста Game Scene в левом верхнем углу
        self.draw_field.draw_field()  # Отрисовка поля
        self.game.score_draw.draw()  # Отрисовка счета
        self.game.life_draw.draw()
        for object in self.objects:
            object.draw()  # Отрисовка пакмана
            object.event()  # Передвижение пакмана
            object.logic(self.objects[0])  # Логика пакмана
import pyray

from objects.Ghost import Ghost
from objects.Pacman import Pacman
from objects.audio import Audio
from scenes.scene import Scene
from objects.text import Text
from scenes.gameoverscene import GameOverScene

class GameScene(Scene):
    def __init__(self, game) -> None:
        super().__init__()
        self.game = game
        self.game.Settings.score_reset()
        self.game.Settings.update_pacman_lifes()
        self.game.Settings.update_gamescene_run_timer()
        self.gamescene_text_object = Text("Game Scene", pyray.Vector2(10, 10), 20, pyray.WHITE)
        self.objects = [
            Pacman(self.game, self.game.Textures.get_texture("images/pacmanup.png"), pyray.Rectangle(409, 335, 18, 18)),
            Ghost(self.game, self.game.Textures.get_texture("images/orangeghostup.png"),
                  pyray.Rectangle(445, 299, 18, 18)),
            Ghost(self.game, self.game.Textures.get_texture("images/pinkghostdown.png"),
                  pyray.Rectangle(415, 299, 18, 18)),
            Ghost(self.game, self.game.Textures.get_texture("images/cyanghostup.png"),
                  pyray.Rectangle(385, 299, 18, 18)),
            Ghost(self.game, self.game.Textures.get_texture("images/redghostleft.png"),
                  pyray.Rectangle(355, 299, 18, 18))]
        self.start_audio = Audio(game, self.game.Settings.get_volume_level())
        self.start_audio.play_track()
        self.win_audio = Audio(game, self.game.Settings.get_volume_level(), "sounds/win_sound.mp3")
        self.game.field.load('field/field.txt')

    def process_input(self) -> None:
        from scenes.pausescene import PauseScene
        if pyray.is_key_pressed(pyray.KeyboardKey.KEY_P):
            self.game.change_scene(PauseScene(self.game, self))
        if self.game.Settings.get_amount_of_seeds() == 0:
            self.game.change_scene(GameOverScene(self.game))
            self.win_audio.play_track()

    def update(self) -> None:
        pass

    def draw(self) -> None:
        self.gamescene_text_object.draw_text()  # Отрисовка текста Game Scene в левом верхнем углу
        self.game.field.draw()  # Отрисовка поля
        self.game.Settings.draw_score()  # Отрисовка счета
        self.game.Settings.draw_pacman_lifes()
        self.game.Settings.add_new_score_to_table()
        self.game.Settings.draw_max()

        for object in self.objects:
            object.draw()  # Отрисовка пакмана
            object.event()  # Передвижение пакмана
            object.logic(self.objects[0])  # Логика пакмана

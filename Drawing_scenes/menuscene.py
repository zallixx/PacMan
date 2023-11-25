import pyray
from Drawing_scenes.scene import Scene
from Drawing_scenes.button import Button
from Drawing_scenes.gamescene import GameScene
from Drawing_scenes.settingsscene import SettingsScene
from Drawing_scenes.pausescene import PauseScene
from HighScore.HighscoreTableDrawer import HighscoreTableDrawer


class MenuScene(Scene):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.buttons = [Button(300, 200, 200, 50, "New Game"),
                        Button(300, 125, 200, 50, "Exit")]
        self.highscore = HighscoreTableDrawer()

    def process_input(self):
        if pyray.is_key_pressed(pyray.KeyboardKey.KEY_ONE):
            self.game.change_scene(GameScene(self.game))
        elif pyray.is_key_pressed(pyray.KeyboardKey.KEY_TWO):
            self.game.change_scene(SettingsScene(self.game))

        for button in self.buttons:
            if button.is_mouse_on_button() and pyray.is_mouse_button_pressed(pyray.MouseButton.MOUSE_BUTTON_LEFT):
                if button.text == "New Game":
                    self.game.change_scene(GameScene(self.game))
                  # Действие кнопки "New Game"
                elif button.text == "Exit":
                    pyray.close_window()

    def update(self):
        pass

    def draw(self):
        pyray.draw_text("Menu Scene", 200, 50, 60, pyray.WHITE)
        self.highscore.draw(325, 275, 18, pyray.WHITE)
        for button in self.buttons:
            button.draw()

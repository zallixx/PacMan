import pyray
from Drawing_scenes.scene import Scene
from Drawing_scenes.button import Button
from Drawing_scenes.gamescene import GameScene
from Drawing_scenes.settingsscene import SettingsScene


class MenuScene(Scene):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.buttons = [Button(300, 200, "New Game"),
                        Button(300, 125, "Exit")]

    def process_input(self) -> None:
        if pyray.is_key_pressed(pyray.KeyboardKey.KEY_ONE):
            self.game.change_scene(GameScene(self.game))
        elif pyray.is_key_pressed(pyray.KeyboardKey.KEY_TWO):
            self.game.change_scene(SettingsScene(self.game))

        for button in self.buttons:
            if button.is_mouse_on_button() and pyray.is_mouse_button_pressed(pyray.MouseButton.MOUSE_BUTTON_LEFT):
                if button.text_in_button == "New Game":
                    self.game.change_scene(GameScene(self.game))
                    self.game.life_draw.lifecount = 3
                # Действие кнопки "New Game"
                elif button.text_in_button == "Exit":
                    pyray.close_window()

    def update(self) -> None:
        pass

    def draw(self) -> None:
        pyray.draw_text("PUCMAN", 275, 50, 60, pyray.WHITE)
        self.game.highscore.draw(325, 275, 18, pyray.WHITE)
        for button in self.buttons:
            button.draw()

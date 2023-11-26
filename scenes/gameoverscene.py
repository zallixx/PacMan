import pyray

from scenes.button import Button
from scenes.scene import Scene
from objects.text import Text


class GameOverScene(Scene):
    def __init__(self, game) -> None:
        super().__init__()
        self.game = game
        self.gameoverscene_text_object = Text("Game Over", 235, 50, 60, pyray.WHITE)
        self.buttons = [Button(300, 200, "Menu"),
                        Button(300, 125, "Exit")]

    def process_input(self) -> None:
        from scenes.menuscene import MenuScene
        for button in self.buttons:
            if button.is_mouse_on_button() and pyray.is_mouse_button_pressed(pyray.MouseButton.MOUSE_BUTTON_LEFT):
                if button.button_text_object.get_text() == "Menu":
                    self.game.change_scene(MenuScene(self.game))
                elif button.button_text_object.get_text() == "Exit":
                    pyray.close_window()
                    pyray.close_audio_device()

    def update(self) -> None:
        pass

    def draw(self) -> None:
        self.gameoverscene_text_object.draw_text()
        for button in self.buttons:
            button.draw()

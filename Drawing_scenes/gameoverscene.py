import pyray
from Drawing_scenes.scene import Scene
from Drawing_scenes.button import Button


class GameOverScene(Scene):
    def __init__(self, game) -> None:
        super().__init__()
        self.game = game
        self.buttons = [Button(300, 200, "Menu"),
                        Button(300, 125, "Exit")]

    def process_input(self) -> None:
        from Drawing_scenes.menuscene import MenuScene
        for button in self.buttons:
            if button.is_mouse_on_button() and pyray.is_mouse_button_pressed(pyray.MouseButton.MOUSE_BUTTON_LEFT):
                if button.text_in_button == "Menu":
                    self.game.change_scene(MenuScene(self.game))
                elif button.text_in_button == "Exit":
                    pyray.close_window()

    def update(self) -> None:
        pass

    def draw(self) -> None:
        pyray.draw_text("Game Over", 235, 50, 60, pyray.WHITE)
        for button in self.buttons:
            button.draw()

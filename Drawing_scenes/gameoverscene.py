import pyray
from Drawing_scenes.scene import Scene
from Drawing_scenes.button import Button


class scene_game_over:
    def __init__(self, width_scene, height_scene, font_size_text):
        self.width_scene = 600
        self.height_scene = 800
        self.font_size_text = 60

    def process_input(self) -> None:
        from Drawing_scenes.menuscene import MenuScene
        for button in self.buttons:
            if button.is_mouse_on_button() and pyray.is_mouse_button_pressed(pyray.MouseButton.MOUSE_BUTTON_LEFT):
                if button.text == "Menu":
                    self.game.change_scene(MenuScene(self.game))
                elif button.text == "Exit":
                    pyray.close_window()


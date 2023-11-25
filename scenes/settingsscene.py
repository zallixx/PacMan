import pyray
from scenes.scene import Scene
from scenes.button import Button
from scenes.pausescene import PauseScene
from scenes.gamescene import GameScene


class SettingsScene(Scene):
    def __init__(self, game, GameScene) -> None:
        super().__init__()
        self.game = game
        self.GameScene = GameScene
        self.game.volume_level = 50
        self.volume_step = 5  # Шаг изменения громкости
        self.buttons = [Button(300, 250, "EXIT")]

    def process_input(self) -> None:
        for button in self.buttons:
            if button.is_mouse_on_button() and pyray.is_mouse_button_pressed(pyray.MouseButton.MOUSE_BUTTON_LEFT):
                if button.text_in_button == "EXIT":
                    self.game.change_scene(PauseScene(self.game, self.GameScene))

        if pyray.is_key_pressed(pyray.KeyboardKey.KEY_UP):
            self.game.volume_level = min(100, self.game.volume_level + self.volume_step)
            # Увеличиваем громкость, ограничивая максимальным значением 100

        elif pyray.is_key_pressed(pyray.KeyboardKey.KEY_DOWN):
            self.game.volume_level = max(0, self.game.volume_level - self.volume_step)
            # Уменьшаем громкость, ограничивая минимальным значением 0

        # pyray.set_sound_volume(pyray.get_default_sound_device(), self.volume_level)

    def update(self) -> None:
        pass

    def draw(self) -> None:
        # Отрисовка сцены настроек
        pyray.draw_text("Settings", 320, 30, 35, pyray.WHITE)
        # Отрисовка уровня громкости
        pyray.draw_text(f"Volume: {self.game.volume_level}", 310, 100, 35, pyray.WHITE)
        for button in self.buttons:
            button.draw()

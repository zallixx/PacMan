import pyray

from objects.audio import Audio
from scenes.scene import Scene
from scenes.button import Button
from scenes.pausescene import PauseScene
from scenes.gamescene import GameScene
from objects.text import Text, RecalculableText


class SettingsScene(Scene):
    def __init__(self, game, GameScene: GameScene) -> None:
        super().__init__()
        self.game = game
        self.settingsscene_text_object = Text("Settings",pyray.Vector2(320, 30), 35, pyray.WHITE)
        self.settingsscene_text_volume = RecalculableText("Volume: {}",pyray.Vector2(310, 100), 35, pyray.WHITE)
        self.GameScene = GameScene
        self.volume_step = 5  # Шаг изменения громкости
        self.buttons = [Button(300, 250, "EXIT")]

    def process_input(self) -> None:
        for button in self.buttons:
            if button.is_mouse_on_button() and pyray.is_mouse_button_pressed(pyray.MouseButton.MOUSE_BUTTON_LEFT):
                if button.button_text_object.get_text() == "EXIT":
                    Audio.update_volume(self.game.Settings.get_volume_level())
                    self.game.change_scene(PauseScene(self.game, self.GameScene))

        if pyray.is_key_pressed(pyray.KeyboardKey.KEY_UP):
            self.game.Settings.change_volume(min(100, self.game.Settings.get_volume_level() + self.volume_step))
            # Увеличиваем громкость, ограничивая максимальным значением 100

        elif pyray.is_key_pressed(pyray.KeyboardKey.KEY_DOWN):
            self.game.Settings.change_volume(max(0, self.game.Settings.get_volume_level() - self.volume_step))
            # Уменьшаем громкость, ограничивая минимальным значением 0

        # pyray.set_sound_volume(pyray.get_default_sound_device(), self.volume_level)

    def update(self) -> None:
        pass

    def draw(self) -> None:
        # Отрисовка сцены настроек
        self.settingsscene_text_object.draw_text()
        # Отрисовка уровня громкости
        print(self.game.Settings.get_volume_level())
        self.settingsscene_text_volume.recreate_text(self.game.Settings.get_volume_level(), "{}")
        self.settingsscene_text_volume.draw_text()
        for button in self.buttons:
            button.draw()

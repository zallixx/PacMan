import pyray
from scenes.scene import Scene
from scenes.button import Button


class PauseScene(Scene):
    def __init__(self, game, GameScene):
        super().__init__()
        self.GameScene = GameScene
        self.game = game
        self.buttons = [Button(300, 250, "Settings"), Button(300, 150, "Main Menu"),
                        Button(300, 350, "Continue")]

    def process_input(self):
        from scenes.menuscene import MenuScene
        from scenes.settingsscene import SettingsScene

        for button in self.buttons:
            if pyray.is_key_pressed(pyray.KeyboardKey.KEY_P):
                self.game.change_scene(self.GameScene)

            if button.is_mouse_on_button() and pyray.is_mouse_button_pressed(pyray.MouseButton.MOUSE_BUTTON_LEFT):
                if button.button_text_object.get_text() == "Continue":
                    self.game.change_scene(self.GameScene)

                elif button.button_text_object.get_text() == "Main Menu":
                    isChanges = False
                    for i in range(0, len(self.game.highscore.highscoreTable.table)):
                        if self.game.highscore.highscoreTable.table[i]['name'] == self.game.PLAYER_NAME:
                            self.game.highscore.highscoreTable.table[i]['score'] = self.game.score_draw.score 
                            isChanges = True
                            self.game.change_scene(MenuScene(self.game))
                        break

                    if not isChanges:
                        self.game.highscore.highscoreTable.add_score(self.game.PLAYER_NAME, self.game.score_draw.score)
                        self.game.change_scene(MenuScene(self.game))

                elif button.button_text_object.get_text() == "Settings":
                    self.game.change_scene(SettingsScene(self.game, self.GameScene))

    def update(self):
        pass

    def draw(self):
        # Отрисовка сцены паузы
        for button in self.buttons:
            button.draw()

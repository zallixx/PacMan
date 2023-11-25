import pyray
from Drawing_scenes.scene import Scene
from Drawing_scenes.button import Button


class PauseScene(Scene):
    def __init__(self, game, GameScene):
        super().__init__()
        self.GameScene = GameScene
        self.game = game
        self.buttons = [Button(300, 300, 200, 50, "Continue"), Button(300, 200, 200, 50, "Main Menu")]

    def process_input(self):
        from Drawing_scenes.menuscene import MenuScene
        for button in self.buttons:
            if pyray.is_key_pressed(pyray.KeyboardKey.KEY_P):
                self.game.change_scene(self.GameScene)
            if button.is_mouse_on_button() and pyray.is_mouse_button_pressed(pyray.MouseButton.MOUSE_BUTTON_LEFT):
                if button.text == "Continue":
                    self.game.change_scene(self.GameScene)
                elif button.text == "Main Menu":
                    self.game.highscore.highscoreTable.add_score(self.game.PLAYER_NAME, self.game.score_draw.score)
                    self.game.change_scene(MenuScene(self.game))

    def update(self):
        pass

    def draw(self):
        # Отрисовка сцены паузы
        pyray.draw_text("Pause Scene", 10, 10, 20, pyray.WHITE)
        for button in self.buttons:
            button.draw()

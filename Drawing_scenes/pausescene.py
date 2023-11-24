import pyray
from Drawing_scenes.scene import Scene
from Drawing_scenes.button import Button



class PauseScene(Scene):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.buttons = [Button(300, 300, 200, 50, "New Game"), Button(300, 200, 200, 50, "Main Menu")]


    def process_input(self):
        from Drawing_scenes.menuscene import MenuScene
        from Drawing_scenes.gamescene import GameScene
        for button in self.buttons:
            if button.is_mouse_on_button() and pyray.is_mouse_button_pressed(pyray.MouseButton.MOUSE_BUTTON_LEFT):
                if button.text == "New Game":
                    #pass
                    self.game.change_scene(GameScene(self.game))
                # Действие кнопки "New Game"
                elif button.text == "Main Menu":
                    #pass
                    self.game.change_scene(MenuScene(self.game))

    def update(self):
        pass

    def draw(self):
        # Отрисовка сцены паузы
        pyray.draw_text("Pause Scene", 10, 10, 20, pyray.BLACK)
        for button in self.buttons:
            button.draw()
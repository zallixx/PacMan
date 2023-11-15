import pyray

class Scene:
    def __init__(self):
        pass

    def process_input(self):
        pass

    def update(self):
        pass

    def draw(self):
        pass


class Button:
    def __init__(self, x, y, width, height, text):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.color = pyray.WHITE

    def draw(self):
        pyray.draw_rectangle(self.x, self.y, self.width, self.height, self.color)
        pyray.draw_text(self.text, self.x + 10, self.y + 10, 20, pyray.BLACK)

    def is_mouse_on_button(self):
        mouse_x, mouse_y = pyray.get_mouse_x(), pyray.get_mouse_y()
        return self.x <= mouse_x <= self.x + self.width and self.y <= mouse_y <= self.y + self.height


class MenuScene(Scene):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.buttons = [Button(300, 300, 200, 50, "New Game"), Button(300, 200, 200, 50, "Exit")]

    def process_input(self):
        if pyray.is_key_pressed(pyray.KeyboardKey.KEY_ONE):
            self.game.change_scene(GameScene(self.game))
        elif pyray.is_key_pressed(pyray.KeyboardKey.KEY_TWO):
            self.game.change_scene(SettingsScene(self.game))

        if pyray.is_key_pressed(pyray.KeyboardKey.KEY_P):
            self.game.change_scene(PauseScene(self.game))

        for button in self.buttons:
            if button.is_mouse_on_button() and pyray.is_mouse_button_pressed(pyray.MouseButton.MOUSE_BUTTON_LEFT):
                if button.text == "New Game":
                    pass  # Действие кнопки "New Game"
                elif button.text == "Exit":
                    pyray.close_window()

    def update(self):
        pass

    def draw(self):
        pyray.draw_text("Menu Scene", 300, 20, 30, pyray.BLACK)
        for button in self.buttons:
            button.draw()

class GameScene(Scene):
    def __init__(self, game):
        super().__init__()
        self.game = game

    def process_input(self):
        pass

    def update(self):
        pass

    def draw(self):
        pyray.draw_text("Game Scene", 10, 10, 20, pyray.BLACK)

class SettingsScene(Scene):
    def __init__(self, game):
        super().__init__()
        self.game = game

    def process_input(self):
        pass

    def update(self):
        pass

    def draw(self):
        # Отрисовка сцены настроек
        pyray.draw_text("Setting Scene", 10, 10, 20, pyray.BLACK)

class PauseScene(Scene):
    def __init__(self, game):
        super().__init__()
        self.game = game

    def process_input(self):
        pass

    def update(self):
        pass

    def draw(self):
        # Отрисовка сцены паузы
        pyray.draw_text("Pause Scene", 10, 10, 20, pyray.BLACK)

class Game:
    def __init__(self):
        self.window_width = 800
        self.window_height = 600
        self.current_scene = MenuScene(self)

    def change_scene(self, scene):
        self.current_scene = scene

    def run(self):
        pyray.init_window(self.window_width, self.window_height, "Pacman Game")

        while not pyray.window_should_close():
            self.current_scene.process_input()
            self.current_scene.update()
            pyray.begin_drawing()
            pyray.clear_background(pyray.RAYWHITE)
            self.current_scene.draw()
            pyray.end_drawing()

        pyray.close_window()


def main() -> None:
    game = Game()
    game.run()

if __name__ == "__main__":
    main()
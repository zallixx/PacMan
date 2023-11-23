import pyray
from Drawing_scenes.menuscene import MenuScene

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
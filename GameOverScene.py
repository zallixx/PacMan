import pyray
from raylib import colors


class scene_game_over:
    def __init__(self, width_scene, height_scene, font_size_text):
        self.width_scene = 600
        self.height_scene = 800
        self.font_size_text = 60

    def draw(self):
        pyray.draw_text(str(GAME OVER), 50, 10, self.font_size_text, colors.WHITE)
        


if __name__ == '__main__':
    main()
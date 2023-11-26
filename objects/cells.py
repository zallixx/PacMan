import pyray
from raylib import colors

from objects.texture import Image


class Empty(Image):
    def __init__(self, game, rect: pyray.Rectangle):
        super().__init__(game, None, rect)


class Wall(Image):
    def __init__(self, game, rect: pyray.Rectangle):
        super().__init__(game, None, rect)

    def draw(self) -> None:
        pyray.draw_rectangle_rec(self.rect, colors.BLUE)


class Teleport(Image):
    teleports = []

    def __init__(self, game, rect: pyray.Rectangle):
        super().__init__(game, None, rect)
        self.teleports.append(self)
        self.index = len(self.teleports) - 1

    def get_next_teleport(self):
        return self.teleports[(self.index + 1) % len(self.teleports)]

    def draw(self):
        pyray.draw_rectangle_rec(self.rect, colors.DARKPURPLE)


class Seed(Image):
    filename = 'images/seed.png'

    def __init__(self, game, rect: pyray.Rectangle):
        super().__init__(game, game.Textures.get_texture(Seed.filename), rect)
        self.rect.x += self.rect.width // 2
        self.rect.y += self.rect.height // 2


class BigSeed(Seed):
    filename = 'images/bigseed.png'

    def __init__(self, game, rect: pyray.Rectangle):
        super().__init__(game, rect)

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
        pass


class Seed(Image):
    filename = 'images/seed.png'

    def __init__(self, game, rect: pyray.Rectangle):
        super().__init__(game, game.Textures.get_texture(Seed.filename), rect)

    def draw(self) -> None:
        source = pyray.Rectangle(0, 0, self.texture.width, self.texture.height)
        dest = pyray.Rectangle(self.rect.x+17, self.rect.y+18, self.texture.width, self.texture.height)
        origin = pyray.Vector2(self.rect.width // 2, self.rect.height // 2)
        pyray.draw_texture_pro(self.texture, source, dest, origin, self.rotation, pyray.WHITE)


class BigSeed(Seed):
    filename = 'images/bigseed.png'

    def __init__(self, game, rect: pyray.Rectangle):
        rect.x = rect.x-3
        rect.y = rect.y-4
        super().__init__(game, rect)
        self.texture = self.game.Textures.get_texture(self.filename)

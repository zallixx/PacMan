from objects.audio import Audio

from objects.cells import *


# Импортим класс для создания объектов из
# Sprite.py(pacman_developer/objects/Classes_of_objects_on_gamescene)
# Для получения большей информации о классе - перейдите в файл


class Pacman(Image):
    def __init__(self, game, texture, rect: pyray.Rectangle) -> None:
        super().__init__(game, texture, rect)
        self.shift = 1
        self.shift_x = self.shift_y = 0
        self.future_x = self.future_y = 0
        self.eat_sound = Audio(self.game, self.game.volume_level / 100, 'sounds/eat_seed_sound.wav')
        self.textures = {"UP": self.game.Textures.get_texture("images/pacmanup.png"),
                         "DOWN": self.game.Textures.get_texture("images/pacmandown.png"),
                         "LEFT": self.game.Textures.get_texture("images/pacmanleft.png"),
                         "RIGHT": self.game.Textures.get_texture("images/pacmanright.png")}
        self.directions = {
            pyray.KeyboardKey.KEY_W: "UP",
            pyray.KeyboardKey.KEY_S: "DOWN",
            pyray.KeyboardKey.KEY_A: "LEFT",
            pyray.KeyboardKey.KEY_D: "RIGHT"
        }  # TODO: Либо мы удалим self.directions, либо же будем использовать -->>
        # TODO: def event на основе self.directions. Как это сделать - предположения есть(уже затестил)

    def event(self) -> None:  # Описывается движение пакмана
        if pyray.is_key_down(pyray.KeyboardKey.KEY_W):
            self.future_y = -self.shift
            self.future_x = 0
        if pyray.is_key_down(pyray.KeyboardKey.KEY_S):
            self.future_y = self.shift
            self.future_x = 0
        if pyray.is_key_down(pyray.KeyboardKey.KEY_A):
            self.future_x = -self.shift
            self.future_y = 0
        if pyray.is_key_down(pyray.KeyboardKey.KEY_D):
            self.future_x = self.shift
            self.future_y = 0
        if pyray.is_key_pressed(pyray.KeyboardKey.KEY_ENTER):
            print(self.shift_x, self.shift_y)

    def move(self):
        self.rect.x += self.shift_x
        self.rect.y += self.shift_y
        self.predict_future()

    def logic(self, pacman) -> None:
        next_tile = self.get_next_tile(self.shift_x, self.shift_y)
        todo = {
            Empty: self.move,
            Wall: self.process_wall,
            Teleport: self.process_teleport,
            Seed: self.process_seed,
            BigSeed: self.process_big_seed
        }
        process = todo[type(next_tile)]
        process()

    def process_seed(self):
        self.game.score_draw.add(10)
        self.move()
        seed = self.get_next_tile(self.shift_x, self.shift_y)
        empty = Empty(self.game, pyray.Rectangle(seed.rect.x, seed.rect.y, seed.rect.width, seed.rect.height))
        self.game.field.set_tile_by_coords(empty)
        self.eat_sound.play_track()

    def get_next_tile(self, shift_x, shift_y):
        if shift_x == 0:
            current_y = (self.rect.y - self.rect.height / 2) if shift_y <= 0 else (
                    self.rect.y + self.rect.height / 2)
            current_x = self.rect.x
        elif shift_y == 0:
            current_x = (self.rect.x - self.rect.width / 2) if shift_x <= 0 else (
                    self.rect.x + self.rect.width / 2)
            current_y = self.rect.y

        next_x = current_x + shift_x
        next_y = current_y + shift_y
        return self.game.field.get_tile_by_coords(next_x, next_y)

    def get_raw_next_tile(self, shift_x, shift_y):
        if shift_x == 0:
            current_y = (self.rect.y - self.rect.height / 2) if shift_y <= 0 else (
                    self.rect.y + self.rect.height / 2)
            current_x = self.rect.x
        elif shift_y == 0:
            current_x = (self.rect.x - self.rect.width / 2) if shift_x <= 0 else (
                    self.rect.x + self.rect.width / 2)
            current_y = self.rect.y

        next_x = current_x + shift_x
        next_y = current_y + shift_y
        return self.game.field.coords_to_clear(next_x, next_y)

    def predict_future(self):
        pacman_rect = pyray.Rectangle(self.rect.x - (self.rect.width // 2),
                                      self.rect.y - (self.rect.height // 2), self.rect.width,
                                      self.rect.height)
        tile_rect = self.game.field.get_tile_by_coords(self.rect.x, self.rect.y).rect

        if pacman_rect.x == tile_rect.x and pacman_rect.y == tile_rect.y and tile_rect.width == pacman_rect.width:
            next_tile = self.get_next_tile(self.future_x, self.future_y)
            if not type(next_tile) == Wall:
                self.shift_x = self.future_x
                self.shift_y = self.future_y
                self.rotate()

    def rotate(self):
        if self.shift_x == self.shift:
            self.texture = self.textures['RIGHT']
        elif self.shift_x == -self.shift:
            self.texture = self.textures['LEFT']
        elif self.shift_y == self.shift:
            self.texture = self.textures['DOWN']
        elif self.shift_y == -self.shift:
            self.texture = self.textures['UP']

    def process_wall(self):
        if self.shift_x > 0 or self.shift_y > 0:
            self.move()
        self.shift_x = self.shift_y = 0

    def process_teleport(self):
        row, col = self.get_raw_next_tile(self.shift_x, self.shift_y)
        if col == 0:
            self.rect.x = 634 - 18
            self.rect.y = 281
        else:
            self.rect.x = 148 + 36
            self.rect.y = 281
        self.move()

    def process_big_seed(self):
        self.game.score_draw.add(10)
        self.process_seed()

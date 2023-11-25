import raylib
from raylib import colors

from Game_objects.Classes_of_objects_on_gamescene.Sprite import Sprite
import pyray

from Game_objects.audio import Audio


# Импортим класс для создания объектов из
# Sprite.py(pacman_developer/Game_objects/Classes_of_objects_on_gamescene)
# Для получения большей информации о классе - перейдите в файл


class Pacman(Sprite):
    def __init__(self, path: str, rect: pyray.Rectangle, game) -> None:
        super().__init__(path, rect)
        self.game = game
        self.eat_sound = Audio(self.game, 0.3, 'sounds/eat_seed_sound.wav')
        self.shift = 1
        self.shift_x = self.shift_y = 0
        self.future_x = self.future_y = 0
        self.textures = {"UP": pyray.load_texture("images/sprites/pacmanup.png"),
                         "DOWN": pyray.load_texture("images/sprites/pacmandown.png"),
                         "LEFT": pyray.load_texture("images/sprites/pacmanleft.png"),
                         "RIGHT": pyray.load_texture("images/sprites/pacmanright.png")}
        self.directions = {
            pyray.KeyboardKey.KEY_W: "UP",
            pyray.KeyboardKey.KEY_S: "DOWN",
            pyray.KeyboardKey.KEY_A: "LEFT",
            pyray.KeyboardKey.KEY_D: "RIGHT"
        }

    def event(self) -> None:
        for key, direction in self.directions.items():
            if pyray.is_key_down(key):
                if direction == "UP":
                    self.coordinate[1] -= 1
                elif direction == "DOWN":
                    self.coordinate[1] += 1
                elif direction == "LEFT":
                    self.coordinate[0] -= 1
                elif direction == "RIGHT":
                    self.coordinate[0] += 1
                self.texture = self.textures[direction]

<<<<<<< Game_objects/Classes_of_objects_on_gamescene/Pacman.py
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
        self.coordinate[0] += self.shift_x
        self.coordinate[1] += self.shift_y
        self.predict_future()

    def logic(self, walls_rectangles: list) -> None:
        next_tile = self.get_next_tile(self.shift_x, self.shift_y)
        match next_tile:
            case 0:
                self.move()
            case 1:
                self.process_wall()
            case 2:
                self.process_teleport()
            case 3:
                self.process_seed()
            case 4:
                self.process_big_seed()
            case _:
                self.move()

    def process_seed(self):
        self.game.current_scene.score_draw.add(10)
        self.move()
        self.game.current_scene.draw_field.set_tile(0, self.get_raw_next_tile(self.shift_x, self.shift_y)[0],
                                                    self.get_raw_next_tile(self.shift_x, self.shift_y)[1])
        self.eat_sound.play_track()

    def get_next_tile(self, shift_x, shift_y):
        if shift_x == 0:
            current_y = (self.coordinate[1] - self.height / 2) if shift_y <= 0 else (
                    self.coordinate[1] + self.height / 2)
            current_x = self.coordinate[0]
        elif shift_y == 0:
            current_x = (self.coordinate[0] - self.width / 2) if shift_x <= 0 else (
                    self.coordinate[0] + self.width / 2)
            current_y=self.coordinate[1]

        next_x = current_x + shift_x
        next_y = current_y + shift_y
        return self.game.current_scene.draw_field.get_tile_by_coords(next_x, next_y)

    def get_raw_next_tile(self, shift_x, shift_y):
        if shift_x == 0:
            current_y = (self.coordinate[1] - self.height / 2) if shift_y <= 0 else (
                    self.coordinate[1] + self.height / 2)
            current_x = self.coordinate[0]
        elif shift_y == 0:
            current_x = (self.coordinate[0] - self.width / 2) if shift_x <= 0 else (
                    self.coordinate[0] + self.width / 2)
            current_y=self.coordinate[1]

        next_x = current_x + shift_x
        next_y = current_y + shift_y
        return self.game.current_scene.draw_field.coords_to_clear(next_x, next_y)

    def predict_future(self):
        pacman_rect = pyray.Rectangle(self.coordinate[0] - self.width / 2,
                                      self.coordinate[1] - self.height / 2, self.width,
                                      self.height)
        tile_rect = pyray.Rectangle(
            148 + (self.game.current_scene.draw_field.coords_to_clear(self.coordinate[0], self.coordinate[1])[
                1]) * 18,
            20 + (self.game.current_scene.draw_field.coords_to_clear(self.coordinate[0], self.coordinate[1])[
                0]) * 18,
            18, 18)
        if pacman_rect.x == tile_rect.x and pacman_rect.y == tile_rect.y and pacman_rect.width == tile_rect.width and pacman_rect.height == tile_rect.height:
            next_tile = self.get_next_tile(self.future_x, self.future_y)
            if not next_tile == 1:
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
        row, col = self.get_raw_next_tile(self.coordinate[0], self.coordinate[1])
        if col == 0:
            self.coordinate = [634 - 18, 272]
        else:
            self.coordinate = [148 + 36, 272]
        self.move()

    def process_big_seed(self):
        self.game.current_scene.score_draw.add(10)
        self.process_seed()
>>>>>>> Game_objects/Classes_of_objects_on_gamescene/Pacman.py

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

        pacman_tile = self.game.current_scene.draw_field.get_tile_by_coords(self.coordinate[0], self.coordinate[1])

        if pacman_tile == 2:
            row, col = self.game.current_scene.draw_field.coords_to_clear(self.coordinate[0], self.coordinate[1])
            if col == 0:
                self.coordinate = [634 - 18, 272]
            else:
                self.coordinate = [148 + 36, 272]

        elif pacman_tile == 3:
            self.game.current_scene.draw_field.set_tile_by_coords(0, self.coordinate[0], self.coordinate[1])
            self.eat_sound.play_track()
            self.game.current_scene.score_draw.add(10)

        elif pacman_tile == 4:
            self.game.current_scene.draw_field.set_tile_by_coords(0, self.coordinate[0], self.coordinate[1])
            self.eat_sound.play_track()
            self.game.current_scene.score_draw.add(145)

    def logic(self, walls_rectangles: list) -> None:
        pacman_rect = pyray.Rectangle(self.coordinate[0] - self.width / 2,
                                      self.coordinate[1] - self.height / 2,
                                      self.width, self.height)
        # Создаем pyray.Rectangle на основе координат пакмана, ширины и высоты

        for wall_rect_data in walls_rectangles:

            # Цикл по списку, содержищий в себе список со следующими значениями:
            # (x, y, self.s, self.s). Где self.s - ширина и высота
            # Сам walls_rectangles создается в списке walls_rectangles который создается в Cell_class.py

            cube_rect = pyray.Rectangle(*wall_rect_data)
            # Создаем pyray.Rectangle на основе списка в списке, полученного в Cell_class.py

            # Проверка на коллизию между пакманом и стеной
            if pyray.check_collision_recs(cube_rect, pacman_rect):

                overlap_x = min(pacman_rect.x + pacman_rect.width, cube_rect.x + cube_rect.width) - max(pacman_rect.x,
                                                                                                        cube_rect.x)
                overlap_y = min(pacman_rect.y + pacman_rect.height, cube_rect.y + cube_rect.height) - max(pacman_rect.y,
                                                                                                          cube_rect.y)
                # Эти две переменные представляют собой размер области,
                # где прямоугольники пересекаются по горизонтали и вертикали соответственно

                # Если перекрытие по оси x меньше, чем по оси y, значит коллизия произошла горизонтально
                if overlap_x < overlap_y:

                    # Проверка на центр пакмана и центр блока по x
                    # Если центр пакмана по x меньше, чем центр куба(стены), то вычитаем overlap_x
                    # Иначе прибавляем overlap_x

                    self.coordinate[0] += -overlap_x if (pacman_rect.x < cube_rect.x) else overlap_x
                else:
                    # Всё то же, но по теперь по y
                    self.coordinate[1] += -overlap_y if (pacman_rect.y < cube_rect.y) else overlap_y

#  Большая часть данного класса взята из лекции(15.11.2023), которую проводил Кучук Егор Андреевич.
#  Выражаю огромную благодарность Егору Андреевичу!

import pyray


class Sprite:
    # Пояснение к данному класу файлу в общем.
    # Данный класс представляет из себя основу всех объектов с текстурами.
    def __init__(self, texture: pyray.load_texture_from_image, rect: pyray.Rectangle) -> None:
        self.coordinate = [rect.x, rect.y]  # Координаты
        self.width = rect.width  # Длина
        self.height = rect.height  # Ширина
        self.texture = texture
        self.rotation = 0  # Поворот текстуры(в градусах)

    def activate(self) -> None:
        pass

    def event(self) -> None:
        pass

    def logic(self) -> None:
        pass

    def draw(self) -> None:
        # Отрисовка объекта(работает для Ghost.py, Pacman.py, Seed_and_Energizer.py).
        source = pyray.Rectangle(0, 0, self.texture.width, self.texture.height)
        dest = pyray.Rectangle(self.coordinate[0], self.coordinate[1], self.width, self.height)
        origin = pyray.Vector2(self.width // 2, self.height // 2)
        pyray.draw_texture_pro(self.texture, source, dest, origin, self.rotation, pyray.WHITE)

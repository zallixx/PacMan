import pyray


class Ghost:  # Общий класс призраков
    def __init__(self, x: int, y: int, color: pyray.Color) -> None:
        self.coordinates = [x, y]
        self.color = color

    def draw(self) -> None:  # Отрисовка призрака. В дальнейшем 20, 20 - размеры призрака(width, height) соответственно.
        # При добавлении текструры в ближайщем будущем придется переписать init у главного класса, добавив texture.
        # Следующим этапом будет изменение данной функции.
        # Придется использовать self.draw_texture(self.texture, self.coordinates[0], self.coordinates[1], pyray.WHITE)
        pyray.draw_rectangle(self.coordinates[0], self.coordinates[1], 20, 20, self.color)


class BlinkyGhost(Ghost):  # Призрак, у которого движение описывается x += 2. То есть движение только вправо
    def __init__(self, x: int, y: int) -> None:
        super().__init__(x, y, pyray.RED)

    def move_and_draw(self) -> None:
        self.coordinates[0] += 2
        super().draw()


class PinkyGhost(Ghost):  # Призрак, у которого движение описывается x -= 2. То есть движение только влево
    def __init__(self, x: int, y: int) -> None:
        super().__init__(x, y, pyray.PINK)

    def move_and_draw(self) -> None:
        self.coordinates[0] -= 2
        super().draw()


class InkyGhost(Ghost):  # Призрак, у которого движение описывается y += 2. То есть движение только вниз
    def __init__(self, x: int, y: int) -> None:
        super().__init__(x, y, pyray.SKYBLUE)

    def move_and_draw(self) -> None:
        self.coordinates[1] += 2
        super().draw()


class ClydeGhost(Ghost):  # Призрак, у которого движение описывается y -= 2. То есть движение только вверх
    def __init__(self, x: int, y: int) -> None:
        super().__init__(x, y, pyray.ORANGE)

    def move_and_draw(self) -> None:
        self.coordinates[1] -= 2
        super().draw()

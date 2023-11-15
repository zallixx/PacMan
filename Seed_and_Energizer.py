import pyray


class Seed:
    def __init__(self, weight: int, x: int, y: int) -> None:
        self.weight = weight
        self.eaten = False
        self.radius = 10
        self.coordinates = [x, y]

    def draw(self) -> None:
        pyray.draw_circle(self.coordinates[0], self.coordinates[1], self.radius, pyray.YELLOW)


class Energizer(Seed):
    def __init__(self, weight: int, x: int, y: int) -> None:
        super().__init__(weight, x, y)
        self.radius = 15

    def draw(self) -> None:
        super().draw()
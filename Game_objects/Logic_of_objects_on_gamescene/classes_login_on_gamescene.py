import pyray

from pacman_developer.Game_objects.Classes_of_objects_on_gamescene.Pacman import Pacman
from pacman_developer.Game_objects.Classes_of_objects_on_gamescene.Ghost import Ghost


class logic_of_pacman:
    def __init__(self):
        self.pacman = Pacman("frog.png", pyray.Rectangle(382, 326, 15, 15))

    def draw(self):
        self.pacman.draw()

    def event(self):
        self.pacman.event()

    def logic(self):
        if self.pacman.coordinate[0] > 795:
            self.pacman.coordinate[0] -= 1
        if self.pacman.coordinate[0] < 5:
            self.pacman.coordinate[0] += 1
        if self.pacman.coordinate[1] > 595:
            self.pacman.coordinate[1] -= 1
        if self.pacman.coordinate[1] < 5:
            self.pacman.coordinate[1] += 1


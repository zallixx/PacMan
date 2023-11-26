#  Большая часть данного класса взята из лекции(15.11.2023), которую проводил Кучук Егор Андреевич.
#  Выражаю огромную благодарность Егору Андреевичу!

import pyray


class Sprite:
    # Пояснение к данному класу файлу в общем.
    # Данный класс представляет из себя основу всех объектов с текстурами.
    def __init__(self, game) -> None:
        self.game = game

    def activate(self) -> None:
        pass

    def event(self) -> None:
        pass

    def logic(self) -> None:
        pass

    def draw(self) -> None:
        pass

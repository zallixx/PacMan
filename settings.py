import pyray


class Settings:
    def __init__(self) -> None:
        self.__width_of_window = 800
        self.__height_of_window = 600
        self.__title_of_window = "Pacman Game"
        self.__volume = 50

    def init_window(self) -> None:
        pyray.init_window(self.__width_of_window, self.__height_of_window, self.__title_of_window)

    def get_width_of_window(self) -> int:
        return self.__width_of_window

    def get_height_of_window(self) -> int:
        return self.__height_of_window

    def get_volume_level(self) -> int:
        return self.__volume

    def change_volume(self, new_volume: int) -> None:
        self.__volume = new_volume


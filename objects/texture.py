import pyray


class Textures:
    def __init__(self) -> None:
        self.list_textures = {}

    def load_and_get_image(self, path: str) -> pyray.load_texture_from_image:
        if path not in self.list_textures:
            pic = pyray.load_image(path)
            texture = pyray.load_texture_from_image(pic)
            pyray.unload_image(pic)
            self.list_textures[path] = ("loaded", texture)
            return texture
        else:
            print("Текстура уже загружена!")

    def unload_image(self, path: str) -> None:
        if path in self.list_textures:
            if self.list_textures[path][1] is not None:
                del self.list_textures[path]
                self.list_textures[path] = ("unloaded", None)
                return
        print("Данной текстуры нет")

    def get_texture(self, path: str) -> pyray.load_texture_from_image:
        if path in self.list_textures:
            if self.list_textures[path][1] is not None:
                return self.list_textures[path][1]
        print("Ошибка при получении текстуры")

    def load_main_textures(self) -> None:
        main_textures_path = ["images/seed.png", "images/bigseed.png", "images/pacmanup.png",
                              "images/orangeghostup.png", "images/pinkghostdown.png", "images/cyanghostup.png",
                              "images/redghostleft.png"]
        for path in main_textures_path:
            pic = pyray.load_image(path)
            texture = pyray.load_texture_from_image(pic)
            pyray.unload_image(pic)
            self.list_textures[path] = ("loaded", texture)

    def clear_textures(self) -> None:
        self.list_textures = {}
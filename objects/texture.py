import pyray


class Textures:
    def __init__(self) -> None:
        self.list_textures = {}

    def load_and_get_image(self, path: str) -> pyray.load_texture_from_image:
        if path not in self.list_textures:
            pic = pyray.load_image(path)
            texture = pyray.load_texture_from_image(pic)
            pyray.unload_image(pic)
            self.list_textures[path] = texture
            return texture
        else:
            print("Текстура уже загружена!")

    def unload_image(self, path: str) -> None:
        if path in self.list_textures:
            del self.list_textures[path]
        print("Данной текстуры нет")

    def get_texture(self, path: str) -> pyray.load_texture_from_image:
        if path in self.list_textures:
            return self.list_textures[path]
        print("Ошибка при получении текстуры")

    def load_main_textures(self) -> None:
        main_textures_path = ["images/seed.png", "images/bigseed.png", "images/pacmanup.png",
                              "images/orangeghostup.png", "images/pinkghostdown.png", "images/cyanghostup.png",
                              "images/redghostleft.png", "images/pacmandown.png", "images/pacmanleft.png",
                              "images/pacmanright.png"]
        for path in main_textures_path:
            if path not in self.list_textures:
                pic = pyray.load_image(path)
                texture = pyray.load_texture_from_image(pic)
                pyray.unload_image(pic)
                self.list_textures[path] = texture

    def clear_textures(self) -> None:
        pass
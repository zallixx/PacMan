import pyray

from field.Field_class import Field
from scenes.menuscene import MenuScene
from objects.texture import Textures
from settings import Settings

class Game:
    def __init__(self) -> None:
        """ Класс игры, позволяющий работать с размерами окна, названием окна, загрузкой текстур, таблицей рекордов, уровнем звука, загрузкой поля
        Далее - объяснение переменных, которые присутствуют в этом классе.
        :param self.current_scene: переменная, которая хранит текущую сцену
        :type self.current_scene: <class Game>
        :param self.Textures: переменная, которая хранит в себе текстуры игры
        :type self.Textures: <class Textures>
        :param self.Settings: переменная, которая хранит в себе инициализацию разных таблиц, счетов, жизний и настроек в общем
        :type self.Settings: <class Settings>
        :param self.Field: переменная, которая хранит поле
        :type self.field: <class Field>
        """
        self.Settings = Settings()
        self.Settings.init_window()
        self.Settings.get_new_player_name()
        self.current_scene = MenuScene(self)
        self.Textures = Textures()
        self.Textures.load_main_textures()
        self.field = Field(
            self,
            (self.Settings.get_width_of_window()-Field.CELL_SIZE * 28) // 2,
            20
        )
        with open("field/field.txt", "r") as file:
            self.fieldTxtStart = file.readlines()
            for i in range(len(self.fieldTxtStart)):
                self.fieldTxtStart[i] = list(self.fieldTxtStart[i][:-1])
            self.fieldTxt = self.fieldTxtStart

    def change_scene(self, scene) -> None:
        """ Функция смены сцены
        :param scene: переменная, которая сцену, на которую надо сменить
        :type scene: <class Game>
        :return: Null
        """
        self.current_scene = scene

    def run(self) -> None:
        """ Функция запуска игры(сцены)
        :return: Null
        """
        pyray.init_audio_device()
        pyray.set_target_fps(120)

        while not pyray.window_should_close():
            self.current_scene.process_input()
            self.current_scene.update()
            pyray.begin_drawing()
            pyray.clear_background(pyray.BLACK)
            self.current_scene.draw()
            pyray.end_drawing()
            self.Settings.save_highscore()

        pyray.close_window()
        pyray.close_audio_device()

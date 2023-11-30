import pyray

from field.Field_class import Field
from scenes.menuscene import MenuScene
from HighScore.HighscoreTableDrawer import HighscoreTableDrawer
from LifeDrawer import LifeDrawer
from ScoreDrawer import ScoreDrawer
from objects.texture import Textures


class Game:
    def __init__(self) -> None:
        """ Класс игры, позволяющий работать с размерами окна, названием окна, загрузкой текстур, таблицей рекордов, уровнем звука, загрузкой поля
        Далее - объяснение переменных, которые присутствуют в этом классе.
        :param self.window_width: ширина окна
        :type self.window_width: int
        :param self.window_height: высота окна
        :type self.window_height: int
        :param self.current_scene: переменная, которая хранит текущую сцену
        :type self.current_scene: <class Game>
        :param self.highscore: переменная, которая хранит в себе таблицу рекордов
        :type self.highscore: <class HighscoreTableDrawer>
        :param self.Textures: переменная, которая хранит в себе текстуры игры
        :type self.Textures: <class Textures>
        :param num: переменная, которая хранит цифру нового игрока
        :type num: int
        :param self.PLAYER_NAME: переменная, которая хранит имя нового игрока
        :type self.PLAYER_NAME: str
        :param self.score_draw: переменная, которая хранит счёт и отрисовывает счёт
        :type self.score_draw: <class ScoreDrawer>
        :param self.life_draw: переменная, которая хранит жизни и отрисовывает их кол-во
        :type self.life_draw: <class LifeDrawer>
        :param self.volume_level: переменная, которая хранит уровень звука
        :type self.volume_level: int
        :param self.Field: переменная, которая хранит поле
        :type self.field: <class Field>
        """
        self.window_width = 800
        self.window_height = 600
        pyray.init_window(self.window_width, self.window_height, "Pacman Game")
        self.current_scene = MenuScene(self)
        self.highscore = HighscoreTableDrawer()
        self.Textures = Textures()
        self.Textures.load_main_textures()
        num = max([int(t['name'][6:]) for t in self.highscore.highscoreTable.table]) + 1
        self.PLAYER_NAME = f"player{num}"
        self.score_draw = ScoreDrawer()
        self.life_draw = LifeDrawer(pyray.Rectangle(680, 30, 18, 18))
        self.volume_level = 50
        self.field = Field(
            self,
            (self.window_width-Field.CELL_SIZE * 28) // 2,
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
        self.highscore.highscoreTable.saveDataToFile()

        pyray.close_window()
        pyray.close_audio_device()

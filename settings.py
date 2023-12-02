import datetime
import pyray
from ScoreDrawer import ScoreDrawer
from HighScore.HighscoreTableDrawer import HighscoreTableDrawer
from LifeDrawer import LifeDrawer


class Settings:
    def __init__(self, game) -> None:
        """ Класс настроек, содержит множества классов и методов
        :param game: все переменные игры
        :type game: Game
        """
        self.game = game

        self.__width_of_window = 800  # Ширина окна
        self.__height_of_window = 600  # Высота окна
        self.__title_of_window = "Pacman Game"  # Название окна
        self.__volume = 1  # Начальный уровень звука
        self.__volume_step = 1  # Сила изменения звука
        self.__highscore = HighscoreTableDrawer()  # Создание таблицы рекордов
        self.__score_draw = ScoreDrawer()  # Создание счета
        self.__score_draw.score = 0  # Присваивание 0 кол-ву счета
        self.__player_name = None  # Имя игрока
        self.__life_draw = None  # Отрисовка жизней
        self.__amount_of_seeds = 242  # Кол-во зёрен
        self.__width_of_lifes = 32  # Ширина текстуры жизни пакмана
        self.__height_of_lifes = 32  # Высота текстуры жизни пакмана
        self.__total_time_after_gamescene_run = None  # Время, когда была запущена игровая сцена
        self.__is_any_cherry_on_scene = False  # Есть ли вишенка на сцене?

    def init_window(self) -> None:
        """Создание окна
        :return: Null
        """
        pyray.init_window(self.__width_of_window, self.__height_of_window, self.__title_of_window)

    def get_width_of_window(self) -> int:
        """Возвращение ширины окна
        :return: int
        """
        return self.__width_of_window

    def get_height_of_window(self) -> int:
        """Возвращение высоты окна
        :return: int
        """
        return self.__height_of_window

    def get_volume_level(self) -> float:
        """Получение уровня звука
        :return: float
        """
        return self.__volume

    def get_volume_step(self) -> int:
        """Получение силы изменения звука
        :return: int
        """
        return self.__volume_step

    def change_volume(self, new_volume: int) -> None:
        """Смена уровня звука
        :param new_volume: новый уровень звука
        :type new_volume: int
        :return: Null
        """
        self.__volume = new_volume

    def get_new_player_name(self) -> None:
        """Получение нового имени игрока
        :return: Null
        """
        num = max([int(t['name'][6:]) for t in self.__highscore.highscoreTable.table]) + 1
        self.__player_name = f"player{num}"

    def draw_highscore(self) -> None:
        """Отрисовка таблицы рекордов
        :return: Null
        """
        self.__highscore.draw(325, 275, 18, pyray.WHITE)

    def draw_max(self) -> None:
        """Отрисовка максиума
        :return: Null
        """
        self.__highscore.draw_max(10, 90, 24, pyray.WHITE)

    def add_new_score_to_table(self) -> None:
        """Добавление игрока и его счета в таблицу
        :return: Null
        """
        self.__highscore.highscoreTable.add_score(self.__player_name, self.__score_draw.score)

    def save_highscore(self) -> None:
        """Сохранение таблицы
        :return: Null
        """
        self.__highscore.highscoreTable.saveDataToFile()

    def draw_score(self) -> None:
        """Отрисовка счета
        :return: Null
        """
        self.__score_draw.draw()

    def add_points_to_score(self, amount: int) -> None:
        """Добавление счета с счету(сложение)
        :param amount: на сколько счет увеличился
        :type amount: int
        :return: Null
        """
        self.__score_draw.add(amount)

    def score_reset(self) -> None:
        """Обнуление счета
        :return: Null
        """
        self.__score_draw.score = 0

    def init_pacman_lifes(self) -> None:
        """Инициализация жизней пакмана
        :return: Null
        """
        self.__life_draw = LifeDrawer(pyray.Rectangle(680, 30, 50, 50),
                                      self.game.Textures.get_texture("images/pacmanleft.png"), self.game)

    def draw_pacman_lifes(self) -> None:
        """Отрисовка жизней пакмана
        :return: Null
        """
        self.__life_draw.draw()

    def get_pacman_lifes(self) -> int:
        """Возвращает кол-во жизней пакмана
        :return: Null
        """
        return self.__life_draw.lifecount

    def remove_pacman_life(self) -> None:
        """Удаление одной жизни
        :return: Null
        """
        self.__life_draw.remove()

    def update_pacman_lifes(self) -> None:
        """Обновление жизней пакмана
        :return: Null
        """
        self.init_pacman_lifes()
        self.__life_draw.lifecount = 3

    def minus_one_seed(self) -> None:
        """-1 к кол-ву зёрен
        :return: Null
        """
        self.__amount_of_seeds -= 1

    def get_amount_of_seeds(self) -> int:
        """Получение кол-во зёрен
        :return: int
        """
        return self.__amount_of_seeds

    def get_width_and_height_of_lifes(self) -> list:
        """Получение ширины и высоты текстуры жизней пакмана
        :return: list
        """
        return [self.__width_of_lifes, self.__height_of_lifes]

    def update_gamescene_run_timer(self) -> None:
        """Обновление таймера, когда была запущена gamescene
        :return: Null
        """
        self.__total_time_after_gamescene_run = datetime.datetime.now()

    def get_gamescene_run_timer(self) -> datetime.datetime.now():
        """Получение таймера
        :return: datetime.datetime.now()
        """
        return self.__total_time_after_gamescene_run

    def get_bool_of_cherry_exsist(self) -> bool:
        """Есть ли вишенка на сцене?
        :return: bool
        """
        return self.__is_any_cherry_on_scene

    def update_cherry_exsist(self) -> None:
        """Обновление существования вишенки на сцене
        :return: None
        """
        if self.__is_any_cherry_on_scene:
            self.__is_any_cherry_on_scene = False
        else:
            self.__is_any_cherry_on_scene = True

    def reset_amount_of_seeds(self) -> None:
        self.__amount_of_seeds = 242

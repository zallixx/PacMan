class ScoreCounter:
    def __init__(self, score_count=0) -> None:
        """ Класс счета, который позволяет работать с добавлением очков к счету
        :param score_count: начальный счет пакмана
        :type score_count: int
        """
        self.score_count = score_count

    def add(self, point: int) -> int:
        """ Функция добавлния очков к счету пакмана
        :param point: кол-во очков, которые следует добавить к счету
        :type point: int
        :return: int
        """
        self.score_count += point
        return self.score_count

class LifeCounter:

    def __init__(self, life_count=3):
        """ Класс жизней пакмана, который позволяет работать с их добавлением и удалением
        :param life_count: кол-во жизней
        :type life_count: int
        """
        self.life_count = life_count

    def add(self) -> int:
        """ Функция добавления жизней у пакмана
        :return: int
        """
        self.life_count += 1
        return self.life_count

    def remove(self) -> float:
        """ Функция убавления жизней у пакмана
        :return: float(or int)
        """
        self.life_count -= 1
        if self.life_count < 0:
            return 1 / 0
        return self.life_count

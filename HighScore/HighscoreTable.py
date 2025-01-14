class HighscoreTable:
    def __init__(self):
        """Таблица рекордов
        """
        self.table = []
        self.loadDataFromFile()
        self.filterTable()
        self.fileName = "HighScore/highscores.txt"

    def loadDataFromFile(self) -> None:
        """Загрузить данные из файла в таблицу рекордов
        :return: Null
        """
        with open("HighScore/highscores.txt", "r", encoding='utf-8') as file:
            listFile = file.readlines()[:10]

            ListFile = [line.split() for line in listFile]

            self.table = [{'name': line[0], 'score': int(line[1])} for line in ListFile]

    def filterTable(self) -> None:
        """Отсортировать по возрастанию таблицу рекордов
        :return: Null
        """
        for i in range(len(self.table) - 1):
            for j in range(len(self.table) - i - 1):
                if self.table[j]['score'] < self.table[j + 1]['score']:
                    self.table[j]['score'], self.table[j +
                                                       1]['score'] = self.table[j + 1]['score'], self.table[j]['score']
                    self.table[j]['name'], self.table[j +
                                                      1]['name'] = self.table[j + 1]['name'], self.table[j]['name']

    def add_score(self, player_name: str, player_score: int) -> None:
        """Добавить счёт в таблицу
        :param player_name: имя игрока
        :type player_name: str
        :param player_score: счёт игрока
        :type player_score: int
        :return: Null
        """
        for i in range(0, len(self.table)):
            if self.table[i]['name'] == player_name:
                if player_score > self.table[i]['score']:
                    self.table[i]['score'] = player_score
                return None

        if len(self.table) == 0:
            self.table.append({'name': player_name, 'score': player_score})
        elif len(self.table) > 0 and (player_score > self.table[-1]['score'] or len(self.table) < 10):
            self.table.append({'name': player_name, 'score': player_score})
            self.filterTable()
            if len(self.table) > 10:
                self.table.pop()

    def saveDataToFile(self) -> None:
        """Сохранить данные в файл
        :return: Null
        """
        with open("HighScore/highscores.txt", "w", encoding='utf-8') as file:
            string = ''
            for i in self.table:
                string += f"{i['name']} {i['score']}\n"
            file.write(string)

    def get_max(self) -> None:
        return max(self.table)

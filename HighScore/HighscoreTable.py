class HighscoreTable:
    def __init__(self):
        """Таблица рекордов
        """
        self.table = []
        self.loadDataFromFile()
        self.filterTable()
        self.fileName = "HighScore/highscores.txt"

    def loadDataFromFile(self):
        """Загрузить данные из файла в таблицу рекордов
        :return: Null
        """
        with open("HighScore/highscores.txt", "r", encoding='utf-8') as file:
            listFile = file.readlines()
            for l in listFile:
                listFile[listFile.index(l)] = l.split()

            for l in listFile:
                self.table.append({'name': l[0], 'score': int(l[1])})

    def filterTable(self):
        """Отсортировать по возрастанию таблицу рекордов
        :return: Null
        """
        for i in range(len(self.table)-1):
            for j in range(len(self.table)-i-1):
                if self.table[j]['score'] < self.table[j+1]['score']:
                    self.table[j]['score'], self.table[j +
                                                       1]['score'] = self.table[j+1]['score'], self.table[j]['score']
                    self.table[j]['name'], self.table[j +
                                                      1]['name'] = self.table[j+1]['name'], self.table[j]['name']

    def add_score(self, player_name: str, player_score: int):
        """Добавить счёт в таблицу
        :param player_name: имя игрока
        :type player_name: str
        :param player_score: счёт игрока
        :type player_score: int
        :return: Null
        """
        if len(self.table) == 0:
            self.table.append({'name': player_name, 'score': player_score})
        elif len(self.table) > 0 and (player_score > self.table[-1]['score'] or len(self.table) < 10):
            self.table.append({'name': player_name, 'score': player_score})
            self.filterTable()
            if len(self.table) > 10:
                self.table.pop()

    def saveDataToFile(self):
        """Сохранить данные в файл
        :return: Null
        """
        with open("HighScore/highscores.txt", "w", encoding='utf-8') as file:
            string = ''
            for i in self.table:
                string += f"{i['name']} {i['score']}\n"
            file.write(string)

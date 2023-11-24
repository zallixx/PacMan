class HighscoreTable:
    def __init__(self):
        self.table = []
        self.loadDataFromFile()
        self.filterTable()
        self.fileName = "HighScore/highscores.txt"

    def loadDataFromFile(self):
        with open("HighScore/highscores.txt", "r", encoding='utf-8') as file:
            listFile = file.readlines()
            for l in listFile:
                listFile[listFile.index(l)] = l.split()

            for l in listFile:
                self.table.append({'name': l[0], 'score': int(l[1])})

    def filterTable(self):
        for i in range(len(self.table)-1):
            for j in range(len(self.table)-i-1):
                if self.table[j]['score'] < self.table[j+1]['score']:
                    self.table[j]['score'], self.table[j +
                                                       1]['score'] = self.table[j+1]['score'], self.table[j]['score']
                    self.table[j]['name'], self.table[j +
                                                      1]['name'] = self.table[j+1]['name'], self.table[j]['name']

    def add_score(self, player_name: str, player_score: int):
        if len(self.table) == 0:
            self.table.append({'name': player_name, 'score': player_score})
        elif len(self.table) > 0 and (player_score > self.table[-1]['score'] or len(self.table) < 10):
            self.table.append({'name': player_name, 'score': player_score})
            self.filterTable()
            if len(self.table) > 10:
                self.table.pop()

    def saveDataToFile(self):
        with open("HighScore/highscores.txt", "w", encoding='utf-8') as file:
            string = ''
            for i in self.table:
                string += f"{i['name']} {i['score']}\n"
            file.write(string)

from collections import deque


class Bfs:
    def __init__(self):
        """ 
        Конструктор класс Bfs
        """
        self.path = []

    def logic(self, field: list, s: tuple, t: tuple, wall: str) -> None:
        """
        Логика поиска кратчайшего пути
        :param field: Двумерный список поля для кратчайшего пути
        :type field: list
        :param s: Стартовая позиция в виде tuple (x, y) 
        :type s: tuple
        :param s: Конечная позиция в виде tuple (x, y) 
        :type s: tuple
        :param wall: Символ стены
        :type wall: str
        """
        n, m = len(field), len(field[0])
        INF = 10 ** 9
        delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        d = [[INF]*m for _ in range(n)]
        used = [[False]*m for _ in range(n)]
        p = [[None]*m for _ in range(n)]
        queue = deque()

        d[s[0]][s[1]] = 0
        used[s[0]][s[1]] = True
        queue.append(s)

        while len(queue) != 0:
            x, y = queue.popleft()
            for dx, dy in delta:
                nx, ny = x + dx, y + dy
                if 0 < nx < n and 0 < ny < m and not used[nx][ny] and field[nx][ny] != wall:
                    d[nx][ny] = d[x][y]+1
                    p[nx][ny] = (x, y)
                    used[nx][ny] = True
                    queue.append((nx, ny))

        cur = t
        path = []
        while cur is not None:
            path.append(cur)
            cur = p[cur[0]][cur[1]]

        path.reverse()
        self.path = list(path)

    def print_map(self, field: list, path=None) -> None:
        if path != None:
            for p in path:
                l = list(field[p[0]])
                l[p[1]] = '*'
                field[p[0]] = ''.join(l)
        for line in field:
            print(*line)
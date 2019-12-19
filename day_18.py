import my

in_data = my.read_input()

width = len(in_data[0])
height = len(in_data)


class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Labirint:
    def __init__(self, matrix):
        self.lab = matrix.copy()
        self.adj = []
        self.__adj()

    def open_door(self, key):
        for i in range(width):
            self.lab[i] = list(map(lambda k: 0 if k == key else k, self.lab[i]))
        self.__adj()

    def __adj(self):
        res = []
        for i in range(width * height):
            x = i % width
            y = i // width

            a = []
            if self.lab[x][y] == 0:  # свободное
                if y > 0 and self.lab[x][y - 1] == 0:
                    a.append(i - width)
                if y < (height - 1) and self.lab[x][y + 1] == 0:
                    a.append(i + width)
                if x > 0 and self.lab[x - 1][y] == 0:
                    a.append(i - 1)
                if x < (width - 1) and self.lab[x + 1][y] == 0:
                    a.append(i + 1)
            res.append(a)

        self.adj = res

    def bfs(self, s):
        level = [-1] * len(self.adj)
        level[s.x * width + s.y] = 0
        # уровень начальной вершины
        queue = [s.x * width + s.y]
        # добавляем начальную вершину в очередь
        while queue:
            # пока там что-то есть
            v = queue.pop(0)
            # извлекаем вершину
            for w in self.adj[v]:
                # запускаем обход из вершины v
                if level[w] is -1:
                    # проверка на посещенность
                    queue.append(w)
                    # добавление вершины в очередь
                    level[w] = level[v] + 1
        return level

    def reachable_keys(self, start:Coordinate, keys):
        level = self.bfs(start)
        return list(map(lambda point: (point, level[point[1].x*width + point[1].y]),
                    filter(lambda elem: level[elem[1].x*width + elem[1].y] != -1, keys.items())))


lab = [[0 for x in range(height)] for y in range(width)]
keys = {}

for j in range(height):
    for i in range(width):
        sym = in_data[j][i]
        if sym == "#":
            lab[i][j] = 1
        elif sym == ".":
            lab[i][j] = 0
        elif sym == "@":
            lab[i][j] = 0
            start = Coordinate(i, j)
        elif sym.islower():
            lab[i][j] = 0
            keys[sym] = Coordinate(i, j)
        elif sym.isupper():
            lab[i][j] = sym.lower()

min_path = 99999999

my_puzzle = Labirint(lab)


def analyze_all_reachable_keys(new_puzzle: object, new_point: Coordinate, new_keys: object, _len: int) -> object:
    global min_path

    if _len > min_path:
        return
    elif len(new_keys.keys()) == 0:
        if _len < min_path:
            min_path = _len
        return

    for reach_key in new_puzzle.reachable_keys(new_point, new_keys):

        print("{}>{}".format("-" * len(new_keys),reach_key[0][0]))

        new_new_puzzle = Labirint(new_puzzle.lab)
        new_new_puzzle.open_door(reach_key[0][0])

        new_new_point = reach_key[0][1]
        new_new_keys = new_keys.copy()
        new_new_keys.pop(reach_key[0][0])
        analyze_all_reachable_keys(new_new_puzzle, new_new_point, new_new_keys, _len + reach_key[1])


analyze_all_reachable_keys(my_puzzle, start, keys, 0)


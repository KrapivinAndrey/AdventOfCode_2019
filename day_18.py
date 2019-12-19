import my


class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Labirint:
    def __init__(self, matrix):
        self.lab = matrix.copy()

        res = []
        for i in range(len(mazze) * len(mazze[0])):
            x = i % width
            y = i // width

            a = []
            if mazze[x][y] == 0:  # свободное
                if y > 0 and mazze[x][y - 1] == 0:
                    a.append(i - width)
                if y < (len(mazze[x]) - 1) and mazze[x][y + 1] == 0:
                    a.append(i + width)
                if x > 0 and mazze[x - 1][y] == 0:
                    a.append(i - 1)
                if x < (len(mazze) - 1) and mazze[x + 1][y] == 0:
                    a.append(i + 1)
            res.append(a)

        self.adj = res

    def open_door(self, key):
        for i in range(width):
            self.lab[i] = list(map(lambda k: 0 if k == key else k, self.lab[i]))

    @staticmethod
    def __start_wave(pathArr):
        weight = 1
        for i in range(len(pathArr) * len(pathArr[0])):
            weight += 1
            for x in range(len(pathArr)):
                for y in range(len(pathArr[x])):
                    if pathArr[x][y] == (weight - 1):
                        if y > 0 and pathArr[x][y - 1] == 0:
                            pathArr[y - 1][x] = weight
                        if y < (len(pathArr[x]) - 1) and pathArr[x][y + 1] == 0:
                            pathArr[x][y + 1] = weight
                        if x > 0 and pathArr[x - 1][y] == 0:
                            pathArr[x - 1][y] = weight
                        if x < (len(pathArr) - 1) and pathArr[x + 1][y] == 0:
                            pathArr[x + 1][y] = weight

    @staticmethod
    def __found(pathArr, finPoint:Coordinate):
        return pathArr[finPoint.x][finPoint.y] > 0

    @staticmethod
    def __printPath(pathArr, finPoint:Coordinate):
        x = finPoint.x
        y = finPoint.y
        weight = pathArr[x][y]
        result = list(range(weight))
        while (weight):
            weight -= 1
            if y < height - 1 and pathArr[x][y + 1] == weight:
                y += 1
                result[weight] = 'down'
            elif y > 0 and pathArr[x][y - 1] == weight:
                result[weight] = 'up'
                y -= 1
            elif x < width - 1 and pathArr[x + 1][y] == weight:
                result[weight] = 'right'
                x += 1
            elif x > 0 and pathArr[x - 1][y] == weight:
                result[weight] = 'left'
                x -= 1

        return result[1:]

    def reachable_keys(self, start:Coordinate, keys):
        path = [[y if y == 0 else -1 for y in x] for x in self.lab]
        path[start.x][start.y] = 1
        self.__start_wave(path)
        return list(map(lambda point: (point, path[point[1].x][point[1].y]), filter(lambda elem: self.__found(path, elem[1]), keys.items())))

    def length_path(self, start:Coordinate, finish:Coordinate):
        temp_map = self.lab.copy()
        path = [[y if y == 0 else -1 for y in x] for x in temp_map]
        path[start.x][start.y] = 1
        if self.__found(path, finish):
            return path[finish.x][finish.y]
        else:
            return -1

in_data = my.read_input()

width = len(in_data[0])
height = len(in_data)


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


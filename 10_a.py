import my
import math


class Vect:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def findClockwiseAngle(self, other):
    # using cross-product formula
        res = -math.degrees(math.asin((self.a * other.b - self.b * other.a)/(self.length()*other.length())))
        # if other.a > 0 and other.b < 0:
        #     res = res + 0
        # elif other.a > 0 and other.b > 0:
        #     res = res + 90
        # elif other.a < 0 and other.b > 0:
        # res = res + 180
        # elif other.a < 0 and other.b < 0:
        return res


    def length(self):
        return math.sqrt(self.a**2 + self.b**2)

    def show(self):
        print(str(self.a+28) + "|" + str(self.b+29))

def nod(x, y):

    a = abs(x)
    b = abs(y)
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a

    gcd = a + b
    return gcd


def cross(a, b, a_new, b_new):
    step_a = a_new - a
    step_b = b_new - b
    gcd = nod(step_a, step_b)
    if gcd == 1:  # взаимнопростые
        return False
    else:
        d_a = int(step_a / gcd)
        d_b = int(step_b / gcd)
        for i in range(1, gcd):
            if map_asteroid[a + d_a * i][b + d_b * i] == '#':
                return True
        return False


def get_visible(x, y):
    count = 0
    if map_asteroid[x][y] != "#":  # строить можно только на астероиде
        return 0
    # решим совсем по тупому. Будем видеть астероид, пока его не заслонит другой через нод
    for i in range(width):
        for j in range(height):
            if i == x and j == y:
                continue
            elif map_asteroid[i][j] != '#':
                continue
            elif not cross(x, y, i, j):
                count += 1
    return count


info = my.read_input()
height = len(info)
width = len(info[0])
map_asteroid = [["." for j in range(height)] for i in range(width)]
for i in range(width):
    for j in range(height):
        map_asteroid[i][j] = info[j][i]

max_count = 0
aster = []

for i in range(width):
    for j in range(height):
        m = get_visible(i,j)
        if m > max_count:
            max_count = m
            aster = [i, j]
print(aster)

import my
import math


class Vect:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def findClockwiseAngle(self, other):
    # using cross-product formula
        res = math.degrees(math.asin((self.a * other.b - self.b * other.a)/(self.length()*other.length())))
        if res == 0 and other.b > 0:
            res = 180
        elif other.a > 0 and other.b < 0:
             res = res + 0
        elif other.a > 0 and other.b > 0:
            res = res + 90
        elif other.a < 0 and other.b > 0:
            res = -res + 180
        elif other.a < 0 and other.b <= 0:
            res = 360 + res
        return res


    def length(self):
        return math.sqrt(self.a**2 + self.b**2)

    def show(self):
        print(str(self.a+X[0]) + "|" + str(self.b+X[1]), end=' ')


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


info = my.read_input()
height = len(info)
width = len(info[0])

map_asteroid = [["." for j in range(height)] for i in range(width)]
for i in range(width):
    for j in range(height):
        map_asteroid[i][j] = info[j][i]

X = [28, 29]
a = Vect(0, -1)


temp = {}
for i in range(width):
    for j in range(height):
        if i == X[0] and j == X[1]:
            continue
        if map_asteroid[i][j] != '#':
            continue
        if cross(X[0], X[1], i, j):
            continue
        b = Vect(i - X[0], j - X[1])
        angle = a.findClockwiseAngle(b)
        if angle in temp:
            temp[angle].append(b)
            temp[angle].sort(key=lambda aster: -1*aster.length(), reverse=True)
        else:
            temp[angle] = [b]

keys = list(temp.keys())
keys.sort()

for i in range(200):
    angle = keys[i]
    asteroid = temp[angle]
    print(i+1, end=' ')
    asteroid[0].show()
    print(angle)
    if len(asteroid) == 1:
        temp.pop(angle)
    else:
        asteroid.pop(0)
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
        print(str(self.a+28) + "|" + str(self.b+29))

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
        if i == 28 and j == 29:
            continue

        b = Vect(i - 28, j - 29)
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
    print(i, end=' ')
    asteroid[0].show()
    if len(asteroid) == 1:
        temp.pop(angle)
    else:
        asteroid.pop(0)
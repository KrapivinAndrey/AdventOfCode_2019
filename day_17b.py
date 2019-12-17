from functools import reduce

import my
import IntcodeComputer
import numpy as np

U = 1
D = 2
L = 3
R = 4
possible_direction = [U, R, D, L]

sym_dir = [1, 4, 2, 3]
UNKNOWN = 0
SCAFFOLD = 1
SPACE = 2
MY_PLACE = 3
MY_PATH = 4
CROSS = 5


class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return str(self.x) + "|" + str(self.y)


class RobotMap:

    def __init__(self):

        self.LEFT = 0
        self.RIGHT = 0
        self.UP = 0
        self.DOWN = 0

        self.xy = {}
        self.put(Coordinate(0, 0), MY_PLACE)

    def put(self, pos: Coordinate, sym):
        if pos.x not in self.xy:
            self.xy[pos.x] = {}

        self.xy[pos.x][pos.y] = sym

        self.LEFT = min(self.LEFT, pos.x)
        self.RIGHT = max(self.RIGHT, pos.x)
        self.UP = max(self.UP, pos.y)
        self.DOWN = min(self.DOWN, pos.y)

    def get(self, pos: Coordinate):
        if pos.x not in self.xy:
            return UNKNOWN
        elif pos.y not in self.xy[pos.x]:
            return UNKNOWN
        else:
            return self.xy[pos.x][pos.y]

    def print(self):

        sym = [' ', '#', '.', 'X', '+', '0']
        j = self.UP
        while j >= self.DOWN:
            for i in range(self.LEFT, self.RIGHT + 1):
                print(sym[self.get(Coordinate(i, j))], end='')
            print()
            j -= 1

class Robot:

    def __init__(self):
        self.pos = Coordinate(0, 0)
        self.map = RobotMap()
        self.path = []

    def get_coordinate(self, dir):
        if dir == U:
            res = Coordinate(self.pos.x, self.pos.y - 1)
        elif dir == D:
            res = Coordinate(self.pos.x, self.pos.y + 1)
        elif dir == L:
            res = Coordinate(self.pos.x - 1, self.pos.y)
        elif dir == R:
            res = Coordinate(self.pos.x + 1, self.pos.y)
        return res

    def get_direction_to(self, new_pos):
        if self.pos.x < new_pos.x:
            return L
        elif self.pos.x > new_pos.x:
            return R
        elif self.pos.y < new_pos.y:
            return U
        elif self.pos.y > new_pos.y:
            return D

    def update_map(self, direction, sym):
        pos = self.get_coordinate(direction)
        self.map.put(pos, sym)

    def move(self, direction):
        self.pos = self.get_coordinate(direction)
        self.path.append(self.pos)

    def what_at_map(self, direction):
        return self.map.get(self.get_coordinate(direction))

    def get_next_move(self):
        for direction in possible_direction:
            if self.what_at_map(direction) in (SCAFFOLD, MY_PATH):
                return direction
        return 'no way'


in_commands = [int(i) for i in my.read_input()[0].split(sep=',')]
comp = IntcodeComputer.IntComputer(in_commands)

comp.pause_input = False
ans = ''

robot = Robot()
i = 0
j = 0
while ans != 'finish':
    ans = comp.run_program()
    if ans == 'output':
        if comp.out_val == 35:
            print("#", end='')
            robot.map.put(Coordinate(i,j), 1)
            i += 1
        elif comp.out_val == 46:
            print(".", end='')
            robot.map.put(Coordinate(i,j), 2)
            i += 1
        elif comp.out_val == 10:
            print()
            i = 0
            j += 1
        else:
            print("^", end='')
            robot.pos = Coordinate(i,j)
            robot.map.put(robot.pos, 3)
            i += 1


def get_opposite(direction):
    if direction in [R, L]:
        return [U, D]
    elif direction in [U, D]:
        return [L, R]


def turn(old, new):
    if (old == U and new == R) or (old == R and new == D) or (old == D and new == L) or (old == L and new == U):
        return "R"
    else:
        return "L"

dir = U
dir_old = U
i = 0
while True:

    next_turn = robot.what_at_map(dir)
    if next_turn in (SCAFFOLD, MY_PATH):
        robot.move(dir)
        i += 1
    elif next_turn in (SPACE, UNKNOWN):
        dir_old = dir
        possible_direction = get_opposite(dir)
        dir = robot.get_next_move()
        if dir == 'no way':
            break
        print(i,)
        i = 0
        print(turn(dir_old, dir),end='')
print(i)

# ABACABCBCB
# A R10R10R6R4
# B R10R10L4
# C R4L4L10L10

main = "A,B,A,C,A,B,C,B,C,B"
A = "R,10,R,10,R,6,R,4"
B = "R,10,R,10,L,4"
C = "R,4,L,4,L,10,L,10"


def ascii_input(in_str):
    temp = list(map(lambda x: ord(x), in_str))
    temp.append(10)
    return temp


in_commands_new = in_commands.copy()
in_commands_new[0] = 2
comp = IntcodeComputer.IntComputer(in_commands_new)
comp.pause_input = True
ans = comp.run_program()
while ans == 'output':
    ans = comp.run_program()

for program in [main, A, B, C]:

    for el in ascii_input(program):
        comp.set_input(el)
        ans = comp.run_program()
    while ans == 'output':
        print(chr(comp.out_val), end='')
        ans = comp.run_program()


# отказ от вывода
ans = comp.run_program()
comp.set_input(110)
ans = comp.run_program()
comp.set_input(10)
while ans == 'output':
    print(chr(comp.out_val), end='')
    ans = comp.run_program()

ans = comp.run_program()
while ans != 'finish':
    ans = comp.run_program()

print(comp.out_val)
from functools import reduce

import my
import IntcodeComputer
import numpy as np

U = 1
D = 2
L = 3
R = 4
possible_direction = [U, R, D, L]

sym_dir = ['', 'U', 'D', 'L', 'R']
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
        old_way = -1
        new_way = -1
        for direction in possible_direction:
            if self.what_at_map(direction) == SCAFFOLD:
                new_way = direction
            elif self.what_at_map(direction) in (MY_PATH, CROSS):
                old_way = direction

        if new_way == -1:
            if old_way == -1:
                return 'no way'
            else:
                return old_way
        else:
            return new_way


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
            print(">", end='')
            robot.pos = Coordinate(i,j)
            robot.map.put(robot.pos, 3)
            i += 1


def get_opposite(direction):
    if direction in [R, L]:
        return [U, D]
    elif direction in [U, D]:
        return [L, R]


dir = U
crosses = []
while True:

    next_turn = robot.what_at_map(dir)
    if next_turn == SCAFFOLD:
        robot.update_map(dir, MY_PATH)
        robot.move(dir)
    elif next_turn == MY_PATH:
        robot.update_map(dir, CROSS)
        crosses.append(robot.get_coordinate(dir))
        robot.move(dir)
    elif next_turn in (SPACE, UNKNOWN):
        possible_direction = get_opposite(dir)
        dir = robot.get_next_move()
        if dir == 'no way':
            break


import my
import IntcodeComputer


def cls(): print("\n" * 100)


UNKNOWN = -2
MY_PLACE = -1
WALL = 0
FREE = 1
OXYGEN = 2

N = 1
S = 2
W = 3
E = 4


class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y


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

        sym = [' ', 'S', '#', '.', 'F']
        j = self.UP
        while j >= self.DOWN:
            for i in range(self.LEFT, self.RIGHT + 1):
                print(sym[2 + self.get(Coordinate(i, j))], end='')
            print()
            j -= 1


class Robot:

    def __init__(self):
        self.pos = Coordinate(0, 0)
        self.map = RobotMap()
        self.path = []
        self.possible_direction = [N, E, S, W]

    def get_coordinate(self, dir):
        if dir == N:
            res = Coordinate(self.pos.x, self.pos.y + 1)
        elif dir == S:
            res = Coordinate(self.pos.x, self.pos.y - 1)
        elif dir == W:
            res = Coordinate(self.pos.x - 1, self.pos.y)
        elif dir == E:
            res = Coordinate(self.pos.x + 1, self.pos.y)
        return res

    def get_direction_to(self, new_pos):
        if self.pos.x < new_pos.x:
            return E
        elif self.pos.x > new_pos.x:
            return W
        elif self.pos.y < new_pos.y:
            return N
        elif self.pos.y > new_pos.y:
            return S

    def update_map(self, direction, sym):
        pos = self.get_coordinate(direction)
        self.map.put(pos, sym)

    def move(self, direction):
        self.pos = self.get_coordinate(direction)
        self.path.append(self.pos)

    def what_at_map(self, direction):
        return self.map.get(self.get_coordinate(direction))

    def get_next_move(self):
        for direction in self.possible_direction:
            if self.what_at_map(direction) == UNKNOWN:
                return direction
        self.path.pop()  # забыли последнюю позицию
        new_pos = self.path.pop()
        if len(self.path) == 0:
            return "no way"
        return self.get_direction_to(new_pos)



in_commands = [int(i) for i in my.read_input()[0].split(sep=',')]

comp = IntcodeComputer.IntComputer(in_commands)
comp.pause_input = True
ans = ''
prev_dir = 0
repair_robot = Robot()
i = 0

start = Coordinate(0, 0)
while ans != 'finish':

    ans = comp.run_program()

    if ans == 'input':

        prev_dir = repair_robot.get_next_move()
        if prev_dir == 'no way':
            break
        comp.set_input(prev_dir)

    elif ans == 'output':

        repair_robot.update_map(prev_dir, comp.out_val)
        if comp.out_val != WALL:
            repair_robot.move(prev_dir)
        if comp.out_val == OXYGEN:
            oxygen_station = repair_robot.pos

repair_robot.map.print()

map = repair_robot.map.xy


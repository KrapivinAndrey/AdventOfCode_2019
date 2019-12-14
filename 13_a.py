import IntcodeComputer
import my
import os
from time import sleep

width = 42
height = 24


class Ball:

    def __init__(self, x, y, dx, dy):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy

    def move(self):

        self.x += self.dx
        self.y += self.dy

    def collapse(self, field, ignore_pad = False):

        # прямой удар

        stop = [1, 2, 3]
        if ignore_pad:
            stop.remove(3)

        if field[self.x + self.dx][self.y] in stop:
            if field[self.x + self.dx][self.y] == 2:
                field[self.x + self.dx][self.y] = 0
            self.dx = -self.dx
            return True
        elif field[self.x][self.y + self.dy] in stop:
            if field[self.x][self.y + self.dy] == 2:
                field[self.x][self.y + self.dy] = 0
            self.dy = -self.dy
            return True
        elif field[self.x + self.dx][self.y + self.dy] in stop:
            if field[self.x + self.dx][self.y + self.dy] == 2:
                field[self.x + self.dx][self.y + self.dy] = 0
            self.dx = -self.dx
            self.dy = -self.dy
            return True
        else:
            return False

    def whereFall(self, field):

        temp_field = field.copy()
        temp_ball = Ball(self.x, self.y, self.dx, self.dy)

        while temp_ball.y != height-2:
            temp_ball.collapse(temp_field, True)
            temp_ball.move()
        return temp_ball.x


class Paddle:

    def __init__(self, x):
        self.x = x
        self.pos = 0

    def move(self):
        if self.x < self.pos:
            self.x += 1
            return 1
        elif self.x > self.pos:
            self.x -= 1
            return -1
        else:
            return 0


game_field = [[0 for i in range(height)] for j in range(width)]

in_commands = [int(i) for i in my.read_input()[0].split(sep=',')]

comp = IntcodeComputer.IntComputer(in_commands)
ans = ''
q = 0

sym_field = [" ", "█", "▓", "▄", "®"]


def get_sym(field):
    return sym_field[field]


clear = lambda: os.system('cls')

def print_field():
    clear()

    for j in range(height):
        for i in range(width):
            print(get_sym(game_field[i][j]), end='')
        print()
    # a = input()


# Считаем поле

while ans != 'finish':
    ans = comp.run_program()
    x = comp.out_val

    ans = comp.run_program()
    y = comp.out_val

    ans = comp.run_program()
    out = comp.out_val
    game_field[x][y] = out
    if out == 3:
        paddle = Paddle(x)
    elif out == 4:
        ball = Ball(x, y, 1, 1)

print_field()
in_commands[0] = 2
comp = IntcodeComputer.IntComputer(in_commands)
comp.pause_input = True
paddle.pos = ball.whereFall(game_field)
print("Pos {}".format(paddle.pos))
ans = ''

while ans != 'finish':

    ans = comp.run_program()

    if ans == "input":
        # comp.set_input(paddle.move())
        # ball.collapse(game_field)
        # ball.move()
        if ball.x < paddle.x:
            comp.set_input(-1)
            paddle.x -= 1
        elif ball.x > paddle.x:
            comp.set_input(1)
            paddle.x += 1
        else:
            comp.set_input(0)

    elif ans == "output":
        x = comp.out_val
        comp.run_program()
        y = comp.out_val

        ans = comp.run_program()
        out = comp.out_val
        if x == -1 and y == 0:

            score = out
            print_field()
            paddle.pos = ball.whereFall(game_field)
            print("Pos {}".format(paddle.pos))
        else:

            game_field[x][y] = out
            if out == 4:
                print("Ball x {}, y {}".format(x, y))
                ball.x = x
                ball.y = y


print("Ans {}".format(score))

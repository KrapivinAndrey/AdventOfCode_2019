from functools import reduce

import IntcodeComputer
import my


in_commands = [int(i) for i in my.read_input()[0].split(sep=',')]

width = 2000


def get_pull(a,b):
    comp = IntcodeComputer.IntComputer(in_commands)
    comp.pause_input = True
    comp.run_program()
    comp.set_input(a)
    comp.run_program()
    comp.set_input(b)
    ans = comp.run_program()
    ans = comp.run_program()
    return str(comp.out_val)


def get_row(y):
    row = reduce(lambda a, x: a + get_pull(x, y), list(range(width)), '')
    return row


def get_board(row):
    x1 = row.find('1')
    x2 = row.find('0', x1)
    return (x1, x2)

y_start = 1100

while True:
    print(y_start)
    up = get_row(y_start)
    down = get_row(y_start + 100)
    b1 = get_board(up)
    b2 = get_board(down)
    if  b2[0] + 100 <= b1[1] or \
        b1[0] - 100 >= b2[0]:
        break
    y_start += 1

print(up)
print(down)
print(b2[0])
print(y_start)
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
    return comp.out_val


def get_row(y):
    row = reduce(lambda a, x: a + get_pull(x, y), list(range(width)), '')
    return row


def get_board(row):
    x1 = row.find('1')
    x2 = row.find('0', x1)
    return (x1, x2)


first_col = 3
last_col = 4
first_cols = {}
last_cols = {}
size = 100
y = 5


while True:
    print(y)
    output = get_pull(first_col, y)
    if output == 0:
        first_col += 1
    output = get_pull(last_col, y)
    if output == 1:
        last_col += 1
    first_cols[y%size] = first_col
    last_cols[y%size] = last_col
    y += 1
    if min(last_cols.values()) - max(first_cols.values()) >=size:
        break

px = min(last_cols.values())-size
py = y - size

print(px*10000+py)
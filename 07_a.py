import IntcodeComputer
import itertools


def read_input():
    res = []
    with open("input.txt") as inf:
        for line in inf:
            res.append(line.strip())
    return res


commands = [int(i) for i in read_input()[0].split(sep=',')]

case = []
new_list = [1, 2, 3, 4, 5]
b = itertools.permutations(new_list, 5)
for i in b:
    case.append(list(i))

max_signal_val = 0
max_signal = []
for test in case:
    prev = 0
    for i in range(5):
        in_val = [test[i], prev]
        IntcodeComputer.commands = commands.copy()
        IntcodeComputer.in_values = in_val.copy()
        prev = IntcodeComputer.run_program()

    if prev > max_signal_val:
        max_signal_val = prev
        max_signal = test.copy()

print(max_signal)
print(max_signal_val)

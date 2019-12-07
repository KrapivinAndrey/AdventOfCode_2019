import IntcodeComputer


def read_input():
    res = []
    with open("input.txt") as inf:
        for line in inf:
            res.append(line.strip())
    return res


IntcodeComputer.commands = [int(i) for i in read_input()[0].split(sep=',')]
IntcodeComputer.in_values = [8]

print(IntcodeComputer.run_program())


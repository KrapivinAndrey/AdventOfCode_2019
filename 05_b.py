import IntcodeComputer


def read_input():
    res = []
    with open("input.txt") as inf:
        for line in inf:
            res.append(line.strip())
    return res


comp = IntcodeComputer.IntComputer([int(i) for i in read_input()[0].split(sep=',')], 10)

comp.run_program()
print(comp.out_val)

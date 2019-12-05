def read_input():
    res = []
    with open("input.txt") as inf:
        for line in inf:
            res.append(line.strip())
    return res


def prepare_comm(comm):
    temp = "{:05d}".format(comm)
    res = [int(temp[-2:]),
            1 if temp[2] == '1' else 0,
            1 if temp[1] == '1' else 0,
            1 if temp[0] == '1' else 0]
    return res


def get_param(point, move):
    param = commands[point + move]
    return commands[param] if comm[move] == 0 else param


commands = [int(i) for i in read_input()[0].split(sep=',')]

step = 0

while True:
    comm = prepare_comm(commands[step])

    if comm[0] == 99:
        break
    elif comm[0] == 1:
        first  = get_param(step, 1)
        second = get_param(step, 2)
        pos    = commands[step + 3]
        commands[pos] = first + second

        step += 4

    elif comm[0] == 2:
        first  = get_param(step, 1)
        second = get_param(step, 2)
        pos    = commands[step + 3]
        commands[pos] = first * second

        step += 4

    elif comm[0] == 3:
        pos    = commands[step + 1]
        commands[pos] = int(input())

        step += 2

    elif comm[0] == 4:
        pos    = get_param(step, 1)
        print(pos)

        step += 2

    elif comm[0] == 5:
        first = get_param(step, 1)
        second = get_param(step, 2)

        if first != 0:
            step = second
        else:
            step += 3

    elif comm[0] == 6:
        first = get_param(step, 1)
        second = get_param(step, 2)

        if first == 0:
            step = second
        else:
            step += 3

    elif comm[0] == 7:
        first = get_param(step, 1)
        second = get_param(step, 2)
        pos    = commands[step + 3]
        commands[pos] = 1 if first < second else 0

        step += 4

    elif comm[0] == 8:
        first = get_param(step, 1)
        second = get_param(step, 2)
        pos    = commands[step + 3]
        commands[pos] = 1 if first == second else 0

        step += 4

    else:
        raise ValueError

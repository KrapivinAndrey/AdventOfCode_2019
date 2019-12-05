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


commands = [int(i) for i in read_input()[0].split(sep=',')]

step = 0
mem = 0
while True:
    comm = prepare_comm(commands[step])

    if comm[0] == 99:
        break
    elif comm[0] == 1:
        first  = commands[step + 1]
        second = commands[step + 2]
        pos    = commands[step + 3]
        commands[pos] = (commands[first] if comm[1] == 0 else first) + (commands[second] if comm[2] == 0 else second)

        step += 4

    elif comm[0] == 2:
        first  = commands[step + 1]
        second = commands[step + 2]
        pos    = commands[step + 3]
        commands[pos] = (commands[first] if comm[1] == 0 else first) * (commands[second] if comm[2] == 0 else second)

        step += 4

    elif comm[0] == 3:
        pos    = commands[step + 1]
        commands[pos] = int(input())

        step += 2

    elif comm[0] == 4:
        pos    = commands[step + 1]
        print(commands[pos])

        step += 2

    else:
        raise ValueError

print(commands)

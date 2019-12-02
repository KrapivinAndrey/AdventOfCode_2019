commands = [int(i) for i in input().split(sep=',')]

step = 0
while True:
    comm = commands[step]
    if comm == 99:
        break
    elif comm == 1:
        first  = commands[step + 1]
        second = commands[step + 2]
        pos    = commands[step + 3]
        commands[pos] = commands[first] + commands[second]

        step += 4
    elif comm == 2:
        first  = commands[step + 1]
        second = commands[step + 2]
        pos    = commands[step + 3]
        commands[pos] = commands[first] * commands[second]

        step += 4
    else:
        raise ValueError

print(commands)

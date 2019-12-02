def run_program(noun, verb, in_commands):
    in_commands[1] = noun
    in_commands[2] = verb
    step = 0
    while True:
        comm = in_commands[step]
        if comm == 99:
            break
        elif comm == 1:
            first = in_commands[step + 1]
            second = in_commands[step + 2]
            pos = in_commands[step + 3]
            in_commands[pos] = in_commands[first] + in_commands[second]

            step += 4
        elif comm == 2:
            first = in_commands[step + 1]
            second = in_commands[step + 2]
            pos = in_commands[step + 3]
            in_commands[pos] = in_commands[first] * in_commands[second]

            step += 4
        else:
            raise ValueError
    return in_commands[0]


commands = [int(i) for i in input().split(sep=',')]
result = 19690720

for i in range(100):
    for j in range(100):
        try:
            if run_program(i, j, commands.copy()) == result:
                print(100 * i + j)
                break
        except ValueError:
            print('Oops')

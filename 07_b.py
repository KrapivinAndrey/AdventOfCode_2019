import IntcodeComputer
import itertools



def read_input():
    res = []
    with open("input.txt") as inf:
        for line in inf:
            res.append(line.strip())
    return res


commands = [int(i) for i in read_input()[0].split(sep=',')]

cases = []
new_list = [5, 6, 7, 8, 9]
b = itertools.permutations(new_list, 5)
for i in b:
    cases.append(list(i))

max_signal_val = 0
max_signal = []
signal = 0

for case in cases:

    amp_a = IntcodeComputer.IntComputer(commands.copy(), case[0])
    amp_a.set_input(0)
    amp_b = IntcodeComputer.IntComputer(commands.copy(), case[1])
    amp_c = IntcodeComputer.IntComputer(commands.copy(), case[2])
    amp_d = IntcodeComputer.IntComputer(commands.copy(), case[3])
    amp_e = IntcodeComputer.IntComputer(commands.copy(), case[4])

    ans = ""
    while ans != "finish":

        ans = amp_a.run_program()

        amp_b.set_input(amp_a.out_val)
        signal = amp_a.out_val
        ans = amp_b.run_program()

        amp_c.set_input(amp_b.out_val)
        signal = amp_b.out_val
        ans = amp_c.run_program()

        amp_d.set_input(amp_c.out_val)
        signal = amp_c.out_val
        ans = amp_d.run_program()

        amp_e.set_input(amp_d.out_val)
        signal = amp_d.out_val
        ans = amp_e.run_program()

        amp_a.set_input(amp_e.out_val)
        signal = amp_e.out_val

    if amp_e.out_val > max_signal_val:
        max_signal_val = amp_e.out_val
        max_signal = case.copy()

print(max_signal)
print(max_signal_val)

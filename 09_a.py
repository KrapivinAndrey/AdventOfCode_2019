import IntcodeComputer
import my


in_commands = [int(i) for i in my.read_input()[0].split(sep=',')]

comp = IntcodeComputer.IntComputer(in_commands)
comp.set_init_val(2)
ans = ''
while ans != 'finish':
    ans = comp.run_program()
print(comp.out_val)

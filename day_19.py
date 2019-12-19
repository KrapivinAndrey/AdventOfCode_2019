import IntcodeComputer
import my


in_commands = [int(i) for i in my.read_input()[0].split(sep=',')]
width = 200
start = 100

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


left = 0
right = width
for y in range(start, width):
    row = ''
    prev_val = 0
    for x in range(0, width):

        if  left-5 < x < right + 5:
            res = get_pull(x, y)
            row += str(res)
            if res != prev_val:
                if prev_val == 0:
                    left = x
                else:
                    right = x
                prev_val = res
        else:
            row += '0'
    print(row)

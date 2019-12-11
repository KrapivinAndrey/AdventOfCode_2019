import IntcodeComputer
import my


class RobotPainter:

    def __init__(self):
        self.x = 0
        self.y = 0
        self.panels = {}
        self.direction = "^"

        self.q_paint = 0
        self.right = 0
        self.left = 0
        self.up = 0
        self.down = 0

    def get_color(self):
        x_y = str(self.x) + "|" + str(self.y)
        if x_y in self.panels:
            return self.panels[x_y]
        else:
            return 0

    def paint(self, color):
        x_y = str(self.x) + "|" + str(self.y)
        if x_y not in self.panels:
            self.q_paint += 1
        self.panels[x_y] = color

    def move(self, output):
        if self.direction == "^":
            if output == 0:  # left 90
                self.x -= 1
                self.direction = "<"
            else: # right 90
                self.x += 1
                self.direction = ">"
        elif self.direction == ">":
            if output == 0:  # left 90
                self.y += 1
                self.direction = "^"
            else:
                self.y -= 1
                self.direction = "V"
        elif self.direction == "V":
            if output == 0:  # left 90
                self.x += 1
                self.direction = ">"
            else:
                self.x -= 1
                self.direction = "<"
        elif self.direction == "<":
            if output == 0:  # left 90
                self.y -= 1
                self.direction = "V"
            else:
                self.y += 1
                self.direction = "^"
        self.left = min(self.left, self.x)
        self.right = max(self.right, self.x)
        self.up = max(self.up, self.y)
        self.down = min(self.down, self.y)


in_commands = [int(i) for i in my.read_input()[0].split(sep=',')]

comp = IntcodeComputer.IntComputer(in_commands)
comp.set_init_val(1)
bot = RobotPainter()
ans = ''
while ans != 'finish':
    comp.run_program()
    bot.paint(comp.out_val)

    ans = comp.run_program()
    bot.move(comp.out_val)

    comp.in_val = bot.get_color()

y = bot.up

while y >= bot.down:
    x = bot.left
    while x <= bot.right:
        x_y = str(x)+"|"+str(y)
        if x_y not in bot.panels:
            out = "0"
        else:
            out = str(bot.panels[x_y])
        print(out, end='')
        x += 1
    print()
    y -= 1


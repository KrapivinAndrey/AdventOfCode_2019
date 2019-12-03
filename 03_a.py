import progressbar


def read_input():
    res = []
    with open("input.txt") as inf:
        for line in inf:
            res.append(line.strip())
    return res


def get_direction(d):
    if d == 'U':
        return 0, 1
    elif d == 'D':
        return 0, -1
    elif d == 'L':
        return -1, 0
    elif d == 'R':
        return 1, 0


path = []
near = 9999999


wires = read_input()

print('First wire')

wire = wires[0]
x = 0
y = 0
steps = wire.split(sep=',')
with progressbar.ProgressBar(len(steps)) as bar:
    for step in steps:
        q = int(step[1:])
        dx, dy = get_direction(step[0])
        for i in range(q):
            x += dx
            y += dy
            point = str(x) + "-" + str(y)
            if point not in path:
                path.append(point)
            bar.update()

print('Second wire')
wire = wires[1]
x = 0
y = 0
steps = wire.split(sep=',')
with progressbar.ProgressBar(len(steps)) as bar:
    for step in steps:
        q = int(step[1:])
        dx, dy = get_direction(step[0])
        for i in range(q):
            x += dx
            y += dy
            point = str(x) + "-" + str(y)
            if point in path:
                if abs(x) + abs(y) < near:
                    near = abs(x) + abs(y)
            else:
                path.append(point)
            bar.update()

print(near)
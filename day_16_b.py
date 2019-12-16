import array
import my
from itertools import cycle


base = [0, 1, 0, -1]


def compute(inp, p):
    return abs(sum(a * b for a, b in zip(inp, p))) % 10


def pattern(reps=1):
    b = cycle(base)
    start = True
    for cur in b:
        for _ in range(reps):
            if start:
                start = False
                continue
            yield cur


def phase(inp):
    for i, val in enumerate(inp):
        yield compute(inp, pattern(i + 1))


phrase = my.read_input()[0]
parsed16 = [int(x) for x in phrase]


def limited_cycle(xs, cycles):
    for _ in range(cycles):
        for x in xs:
            yield x

offset = int("".join(phrase[:7]))


def endphase(inp):
    n = []
    s = 0
    for i in inp[::-1]:
        s += i
        n.append(abs(s) % 10)
    return n[::-1]


def endfft(inp, offset, phases):
    inp = inp[offset:]
    for _ in range(phases):
        inp = endphase(inp)
    return inp


print(endfft(list(limited_cycle(parsed16, 10000)), offset, 100)[:8])
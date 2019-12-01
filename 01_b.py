from math import *
import sys


def fuel(mass):
    need = floor(mass/3) - 2

    if need <= 0:
        return 0
    else:
        return need + fuel(need)


s = sum(fuel(int(i)) for i in sys.stdin.read().split())

print(s)

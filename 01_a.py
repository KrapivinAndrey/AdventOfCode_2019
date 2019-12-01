from math import *
import sys


def fuel(mass):
    return floor(mass/3) - 2


s = sum(fuel(int(i)) for i in sys.stdin.read().split())

print(s)

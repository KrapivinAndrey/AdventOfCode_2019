from functools import reduce

import my


def get_pattern(step):
    pattern = [0, 1, 0, -1]
    return [y for x in pattern for y in (x,) * step]


def apply_pattern(in_str: str, pattern: list):

    len_pattern = len(pattern)
    res = reduce(lambda a, x: a + int(x[1]) * pattern[(x[0] + 1) % len_pattern], list(enumerate(list(in_str))), 0)
    return str(res)[-1::1]


def phase(in_str: str):
    res = ''
    for i in range(1, len(in_str) + 1):
        res += apply_pattern(in_str, get_pattern(i))
    return res


def run_phase(in_str: str, step: int):
    a = in_str
    for i in range(step):
        print('step {}'.format(i))
        a = phase(a)
    return str(a)


phrase = my.read_input()[0]
print(run_phase(phrase, 100)[:8:])

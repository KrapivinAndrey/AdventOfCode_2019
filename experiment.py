from functools import reduce

in_str = '98765'
print(list(enumerate(list(in_str))))

res = reduce(lambda a, x: a + int(x[1])*x[0], list(enumerate(list(in_str))), 0)
print(res)
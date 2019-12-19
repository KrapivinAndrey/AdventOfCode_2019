from functools import reduce

a = list(range(5))
s = reduce(lambda a,x:a+str(x),list(range(5)),'')
print(s)
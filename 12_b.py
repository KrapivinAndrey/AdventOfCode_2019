import math
a, b = int(input()), int(input())
print(a * b // math.gcd(a, b))
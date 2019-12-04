def read_input():
    res = []
    with open("input.txt") as inf:
        for line in inf:
            res.append(line.strip())
    return res


def has_double(password):
    double = ['00', '11', '22', '33', '44', '55', '66', '77', '88', '99']
    return any(a in str(password) for a in double)


def increase(password):
    prev = 0
    for digit in str(password):
        if int(digit) < prev:
            return False
        prev = int(digit)
    return True


def correct_password(password):
    return has_double(password) and increase(password)


bound = [int(i) for i in read_input()[0].split(sep='-')]
ans=0

for i in range(int(bound[0]), int(bound[1]) + 1):
    if correct_password(i):
        ans += 1

print(ans)

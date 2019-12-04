def read_input():
    res = []
    with open("input.txt") as inf:
        for line in inf:
            res.append(line.strip())
    return res


def has_repeat(password):
    prev = password[0]
    d = 0
    q = 1

    for i in range(1, 6):
        if prev != password[i]:
            prev = password[i]
            if q == 2:
                d += 1
            q = 1
        else:
            q += 1
    if q == 2:
        d += 1
    return d > 0


def increase(password):
    prev = 0
    for digit in password:
        if int(digit) < prev:
            return False
        prev = int(digit)
    return True


def correct_password(password):
    return has_repeat(password) and increase(password)


bound = [int(i) for i in read_input()[0].split(sep='-')]
ans=0

for i in range(int(bound[0]), int(bound[1]) + 1):
    if correct_password(str(i)):
        print(str(i))
        ans += 1

print(ans)

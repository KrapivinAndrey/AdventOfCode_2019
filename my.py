def read_input():
    res = []
    with open("input.txt") as inf:
        for line in inf:
            res.append(line.strip())
    return res
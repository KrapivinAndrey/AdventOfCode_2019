import my


def parse_layer(pixels):

    res = []

    pixels = str(pixels).strip()
    k = 0
    for i in range(int((len(pixels) / (width * height)))):
        a = []
        for j in range(height):
            a.append(pixels[2 + k * width: 2 + (k+1) * width].strip())
            k += 1
        res.append(a)
    return res


def find_answer():
    min_zero = 25 * 7
    ans = 0
    for layer in img:
        zero = 0
        q_one = 0
        q_two = 0
        for i in range(height):
            zero += layer[i].count('0')
            q_one += layer[i].count('1')
            q_two += layer[i].count('2')
        if zero < min_zero:
            min_zero = zero
            ans = q_one * q_two

    return ans


def decode():
    res = [[2 for j in range(width)] for i in range(height)]
    for layer in img:
        for i in range(height):
            for j in range(width):
                if res[i][j] == 2 and int(layer[i][j]) != 2:
                    res[i][j] = int(layer[i][j])
    print(res)


width  = 25
height = 6

img_signal = my.read_input()
img = parse_layer(img_signal)

decode()
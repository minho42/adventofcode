from utils import read_input

lines = read_input("2022_4_input.txt")


def p1():
    count = 0

    for line in lines:
        a, b, c, d = [int(x) for x in line.replace(",", " ").replace("-", " ").split()]
        if (a <= c and b >= d) or (a >= c and b <= d):
            count += 1

    print(count)


def p2():
    count = 0

    for line in lines:
        a, b, c, d = [int(x) for x in line.replace(",", " ").replace("-", " ").split()]
        if (a < c and b < c) or (a > c and a > d):
            continue
        count += 1

    print(count)


p1()
p2()

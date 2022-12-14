from utils import read_input

lines = read_input("10.in")


def p1():
    cycles = [20, 60, 100, 140, 180, 220]
    total = []
    r = 1
    i = 1

    for line in lines:
        match line.split():
            case ["addx", x]:
                x = int(x)
                i += 2
                try:
                    if i > cycles[0]:
                        total.append(cycles[0] * r)
                        cycles.pop(0)
                except IndexError:
                    break
                r += x
            case ["noop"]:
                i += 1

    # print(total)
    print(sum(total))


def p2():
    crt = []
    r = 1
    i = 0

    for line in lines:
        sprites = [r - 1, r, r + 1]
        match line.split():
            case ["addx", x]:
                x = int(x)
                for _ in range(2):
                    if i in sprites:
                        crt.append("#")
                    else:
                        crt.append(".")
                    i += 1
                    i %= 40
                r += x
            case ["noop"]:
                if i in sprites:
                    crt.append("#")
                else:
                    crt.append(".")
                i += 1
                i %= 40

    for i, c in enumerate("".join(crt), start=1):
        if i % 40 == 0:
            print(c)
        else:
            print(c, end="")


p1()
p2()

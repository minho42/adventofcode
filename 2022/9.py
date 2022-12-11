from utils import read_input

lines = read_input("9.in")


def right(a):
    a[1] += 1


def left(a):
    a[1] -= 1


def up(a):
    a[0] -= 1


def down(a):
    a[0] += 1


def should_tail_move(h, t):
    return abs(h[0] - t[0]) > 1 or abs(h[1] - t[1]) > 1


def follow(h, t):
    # horizontal
    if h[0] == t[0]:
        if h[1] > t[1]:
            right(t)
        else:
            left(t)
    # vertical
    elif h[1] == t[1]:
        if h[0] > t[0]:
            down(t)
        else:
            up(t)
    # diagonal
    else:
        if h[0] < t[0]:
            up(t)
        else:
            down(t)

        if h[1] < t[1]:
            left(t)
        else:
            right(t)


move_to = {"R": right, "L": left, "U": up, "D": down}


def p(n):
    h = [0, 0]
    t = []
    t.append(h)
    for _ in range(n):
        t.append([0, 0])

    visited = []
    for line in lines:
        direction, count = line.split()
        for _ in range(int(count)):
            move_to[direction](t[0])
            for i in range(n):
                try:
                    if should_tail_move(t[i], t[i + 1]):
                        follow(t[i], t[i + 1])

                except IndexError:
                    break
            visited.append(str(t[-1][0]) + "," + str(t[-1][1]))

    visited_unique = set(visited)
    print(len(visited_unique))


p(1)
p(9)

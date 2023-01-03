from utils import read_input
from collections import defaultdict

winds = read_input("17.in")

landed_rocks = [
    [-1, 0],
    [-1, 1],
    [-1, 2],
    [-1, 3],
    [-1, 4],
    [-1, 5],
    [-1, 6],
]


def can_move_horizontally(r, direction):
    temp = []
    lr = 0
    if direction == ">":
        lr = 1
    else:
        lr = -1
    for x in r:
        temp.append([x[0], x[1] + lr])
    if any([x in landed_rocks for x in temp]):
        return False
    if any([x for x in temp if x[1] < 0 or x[1] > 6]):
        return False

    return True


def can_go_down(r):
    temp = []
    for x in r:
        temp.append([x[0] - 1, x[1]])

    return not any([x in landed_rocks for x in temp])


def clear():
    d = defaultdict(set)
    [d[k].add(v) for k, v in landed_rocks]

    max = 0
    for k, v in d.items():
        if len(v) == 7 and k > max:
            max = k

    for x in landed_rocks:
        if x[0] < max:
            landed_rocks.remove(x)


def down(r):
    if can_go_down(r):
        for x in r:
            x[0] -= 1
    else:
        [landed_rocks.append(x) for x in r if x not in landed_rocks]
        # clear()


def get_highest_rock():
    temp = [x[0] for x in landed_rocks]
    return max(temp) + 1


def get_new_rock(i):
    h = get_highest_rock()

    j = i % 5

    if j == 0:
        r = [[h + 3, 2], [h + 3, 3], [h + 3, 4], [h + 3, 5]]
    elif j == 1:
        r = [
            [h + 3, 3],
            [h + 4, 2],
            [h + 4, 3],
            [h + 4, 4],
            [h + 5, 3],
        ]
    elif j == 2:
        r = [[h + 3, 2], [h + 3, 3], [h + 3, 4], [h + 4, 4], [h + 5, 4]]
    elif j == 3:
        r = [[h + 3, 2], [h + 4, 2], [h + 5, 2], [h + 6, 2]]
    elif j == 4:
        r = [[h + 3, 2], [h + 3, 3], [h + 4, 2], [h + 4, 3]]
    else:
        raise
    return r


def is_landed(r):
    for x in r:
        if x in landed_rocks:
            return True
    return False


def move_horizontally(r, wi):
    direction = winds[wi % len(winds)]
    if can_move_horizontally(r, direction):
        if direction == ">":
            for x in r:
                x[1] += 1
        else:
            for x in r:
                x[1] -= 1


def p1():

    i = 0
    ri = 0
    wi = 0
    while True:
        r = get_new_rock(ri)
        while not is_landed(r):
            if i % 2 == 0:
                move_horizontally(r, wi)
                wi += 1
            else:
                down(r)
            i += 1

        ri += 1
        if ri >= 2022:
            # if ri >= 1000000000000:
            break

    print(get_highest_rock())


p1()

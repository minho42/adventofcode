from utils import read_input

lines = read_input("2022_8.in")


def is_edge(d, i, j):
    return (i == 0 or i == len(d) - 1) or (j == 0 or j == len(d[0]) - 1)


def is_visible_horizontally(li: list, me):
    return me > max(li)


def is_visible_vertically(d, i, j, me):
    li = [d[x][j] for x in range(i + 1) if x < i]
    li2 = [d[x][j] for x in range(len(d)) if x > i]

    return is_visible_horizontally(li, me) or is_visible_horizontally(li2, me)


def is_visible(d, i, j):
    if is_edge(d, i, j):
        return True

    me = d[i][j]

    return any(
        [
            is_visible_horizontally(d[i][:j], me),
            is_visible_horizontally(d[i][j + 1 :], me),
            is_visible_vertically(d, i, j, me),
        ]
    )


def p1():
    count = 0
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if is_visible(lines, i, j):
                # print(f"[{i}][{j}]: {lines[i][j]}")
                count += 1

    print(count)


p1()

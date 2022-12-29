from utils import read_input

lines = read_input("20.in")


def p(cycle, key):
    d = []

    for i, line in enumerate(lines):
        # Saves original index (order for movement) for item as a tuple in a list
        # e.g. [(1, 0), (2, 1), (-3, 2), (3, 3), (-2, 4), (0, 5), (4, 6)]
        d.append((int(line) * key, i))

    def find_next_item(i):
        for xi, x in enumerate(d):
            if x[1] == i:
                return xi, x
        raise

    def find_index_by_value(v):
        for xi, x in enumerate(d):
            if x[0] == v:
                return xi
        raise

    for _ in range(cycle):
        for i in range(len(lines)):
            ii, item = find_next_item(i)

            if item[0] == 0:
                continue

            d.pop(ii)
            new_i = (ii + item[0]) % len(d)
            if new_i == 0:
                new_i = len(d)

            d.insert(new_i, item)

    zero_i = find_index_by_value(0)
    a = (zero_i + 1000) % len(d)
    b = (zero_i + 2000) % len(d)
    c = (zero_i + 3000) % len(d)

    sum = 0

    for x in [a, b, c]:
        sum += d[x][0]

    print(sum)


p(1, 1)
p(10, 811589153)

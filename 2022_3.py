def get_priority(c: str) -> int:
    # priorities
    # a-z: 1-26
    # A-Z: 27-52
    # ord('a') == 97
    # ord('A') == 65
    priority = 0
    if c.islower():
        priority = ord(c) - 96
    else:
        priority = ord(c) - 38
    return priority


def part1():
    common_items = []

    def find_common_item(line: str) -> str:
        middle = len(line) // 2
        first = line[:middle]
        second = line[middle:]

        for x in first:
            if x in second:
                return x

    with open("2022_3.in") as file:
        for line in file:
            line = line.replace("\n", "")
            common_items.append(find_common_item(line))

    sum = 0
    for x in common_items:
        sum += get_priority(x)
    print(sum)


def part2():
    common_items = []

    def find_common_item(lines: list) -> str:
        first = lines[0]
        second = lines[1]
        third = lines[2]

        for x in first:
            if x in second and x in third:
                return x

    with open("2022_3.in") as file:
        lines = []
        for index, line in enumerate(file):
            line = line.replace("\n", "")
            lines.append(line)

            if index % 3 == 2:
                common_items.append(find_common_item(lines))
                lines = []

    sum = 0
    for x in common_items:
        sum += get_priority(x)
    print(sum)


part1()
part2()

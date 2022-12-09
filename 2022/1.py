# https://adventofcode.com/2022/day/1
# https://adventofcode.com/2022/day/1/input

# Added newline at the end of the input to make it easy

current_sum = 0
list_of_sums = []

with open("1.in") as file:
    for line in file:
        line = line.replace("\n", "")
        if line:
            current_sum += int(line)
        else:
            if current_sum > 0:
                list_of_sums.append(current_sum)
            current_sum = 0


def part1():
    print(max(list_of_sums))


def part2():
    top_sums = []
    for _ in range(3):
        temp_max = max(list_of_sums)
        list_of_sums.remove(temp_max)
        top_sums.append(temp_max)
    print(sum(top_sums))


part1()
part2()

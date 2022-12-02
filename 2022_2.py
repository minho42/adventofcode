# https://adventofcode.com/2022/day/2
# https://adventofcode.com/2022/day/2/input

# A: Rock ✊
# B: Paper 🖐
# C: Scissors ✌️

outcome_scores = {"LOSS": 0, "DRAW": 3, "WIN": 6}
shape_scores = {"A": 1, "B": 2, "C": 3}

winning_conditions = ["AB", "BC", "CA"]
losing_conditions = ["AC", "BA", "CB"]
drawing_conditions = ["AA", "BB", "CC"]

occurrence_counts = {}

with open("2022_2_input.txt") as file:
    for line in file:
        line = line.replace("\n", "")
        line = line.replace(" ", "")

        # Swab "XYZ" -> "ABC"
        line = line.replace("X", "A")
        line = line.replace("Y", "B")
        line = line.replace("Z", "C")

        # Count occurrence of each combinations
        if line in occurrence_counts:
            occurrence_counts[line] += 1
        else:
            occurrence_counts[line] = 1


def get_outcome_score(match: str) -> int:
    score = 0
    if match in winning_conditions:
        score += outcome_scores["WIN"]
    elif match in losing_conditions:
        score += outcome_scores["LOSS"]
    elif match in drawing_conditions:
        score += outcome_scores["DRAW"]
    return score


def get_shape_score(match: str) -> int:
    return shape_scores[match[1]]


def get_round_score(match: str) -> int:
    return get_outcome_score(match) + get_shape_score(match)


def part1():
    total_score = 0
    for match, count in occurrence_counts.items():
        total_score += get_round_score(match) * count
    print(total_score)


def get_new_match(match: str) -> str:
    new_match = ""

    guide = match[1]
    if guide == "A":
        # A: to lose
        new_match = [c for c in losing_conditions if c.startswith(match[0])][0]
    elif guide == "B":
        # B: to draw
        new_match = [c for c in drawing_conditions if c.startswith(match[0])][0]
    elif guide == "C":
        # C: to win
        new_match = [c for c in winning_conditions if c.startswith(match[0])][0]

    return new_match


def part2():
    total_score = 0
    for match, count in occurrence_counts.items():
        total_score += get_round_score(get_new_match(match)) * count
    print(total_score)


part1()
part2()

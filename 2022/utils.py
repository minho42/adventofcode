from typing import Union


def read_input(path: str) -> Union[list, str]:
    with open(path, "r") as f:
        contents = f.read()
        lines = contents.split("\n")
    if len(lines) == 1:
        return lines[0]
    return lines

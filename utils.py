def read_input(path: str) -> list:
    with open(path, "r") as f:
        contents = f.read()
        lines = contents.split("\n")
    return lines

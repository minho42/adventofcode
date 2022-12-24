import re
from sympy import Symbol
from sympy.solvers import solve
from utils import read_input

lines = read_input("21.in")

d = {}

for line in lines:
    line = line.replace(":", "=").replace(" ", "")
    a, b = line.split("=")
    d[a] = b


def f(x):
    if d[x].isdigit():
        return d[x]
    return f"( {f(d[x][:4])} ) {d[x][4]} ( {f(d[x][5:])} )"


p1 = f("root")
p1 = eval(p1)
p1 = int(p1)
print(p1)


def f2(x):
    if "humn" in x:
        return x
    if d[x].isdigit():
        return d[x]
    m = re.search(r"(\w+)([=+\-*\/]{1,})(\w+)", d[x])
    return f"({f2(m[1])}) {m[2]} ({f2(m[3])})"


# root = x + humn
# x = root - humn
d["root"] = d["root"].replace("+", "-")
d["humn"] = "humn"
p2 = f2("root")
p2 = solve(p2)[0]
print(p2)

from utils import read_input
from collections import deque

lines = read_input("05.in")


def p1():
    stack = [
        "💩",
        deque("BLDTWCFM"),
        deque("NBL"),
        deque("JCHTLV"),
        deque("SPJW"),
        deque("ZSCFTLR"),
        deque("WDGBHNZ"),
        deque("FMSPVGCN"),
        deque("WQRJFVCZ"),
        deque("RPMLH"),
    ]
    for line in lines[10:]:
        i = line.split(" ")
        # "move 5 from 3 to 6"
        # a = 5, b = 3, c = 6
        a, b, c = int(i[1]), int(i[3]), int(i[5])
        for _ in range(a):
            stack[c].append(stack[b].pop())

    r = ""
    for s in stack[1:]:
        r += s[-1]
    print(r)


def p2():
    stack = [
        "💩",
        deque("BLDTWCFM"),
        deque("NBL"),
        deque("JCHTLV"),
        deque("SPJW"),
        deque("ZSCFTLR"),
        deque("WDGBHNZ"),
        deque("FMSPVGCN"),
        deque("WQRJFVCZ"),
        deque("RPMLH"),
    ]

    for line in lines[10:]:
        i = line.split(" ")
        a, b, c = int(i[1]), int(i[3]), int(i[5])
        for _ in range(a):
            stack[c].appendleft(stack[b].pop())
        stack[c].rotate(-a)

    r = ""
    for s in stack[1:]:
        r += s[-1]
    print(r)


p1()
p2()

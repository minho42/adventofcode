from utils import read_input

d = read_input("2022_6.in")


def p(n):
    for i in range(len(d)):
        try:
            s = set([d[i + x] for x in range(n)])
            if len(s) == n:
                print(i + n)
                break
        except IndexError:
            break


p(4)
p(14)

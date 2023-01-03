from utils import read_input

lines = read_input("25.in")

a = []
for x in range(25):
    n = 1
    for y in range(x):
        n *= 5
    a.append(n)

r = 0

for line in lines:
    for i, x in enumerate(line[::-1]):
        match x:
            case "-":
                r -= a[i]
            case "=":
                r -= a[i] * 2
            case "0":
                continue
            case _:
                r += a[i] * int(x)

print(r)


def decimal_to_snafu(n):
    r = ""

    closest = lambda x: abs(x - n)
    start_i = a.index(min(a, key=closest))

    chars = "012-="
    for x in a[: start_i + 1][::-1]:
        # chars and options orders to be matched
        options = [
            n,
            n - (x),
            n - (x * 2),
            n + (x),
            n + (x * 2),
        ]
        close_to_zero = min(options, key=lambda x: abs(x))
        oi = options.index(close_to_zero)
        n = close_to_zero
        r += chars[oi]

    return r


p1 = decimal_to_snafu(r)
print(p1)

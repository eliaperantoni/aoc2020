from itertools import product

lines = open("input.txt").readlines()
lines = map(lambda line: int(line), lines)
lines = list(lines)

for a, b, c in product(lines, lines, lines):
    if a + b + c == 2020:
        print(a*b*c)
        break

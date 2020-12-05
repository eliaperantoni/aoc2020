from itertools import product

lines = open("input.txt").readlines()
lines = map(lambda line: int(line), lines)
lines = list(lines)

for a, b in product(lines, lines):
    if a + b == 2020:
        print(a*b)
        break

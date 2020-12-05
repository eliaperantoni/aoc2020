m = open("input.txt").readlines()

lines_count = len(m)

REPEAT_COUNT = 200


def replicate(line):
    return line.strip() * REPEAT_COUNT


m = list(map(replicate, m))


def at(x, y):
    return m[y][x]


pos = (0, 0)

trees = 0

while pos[1] < lines_count:
    if at(*pos) == "#":
        trees += 1

    pos = (pos[0] + 3, pos[1] + 1)

print(trees)

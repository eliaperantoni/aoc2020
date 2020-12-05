m = open("input.txt").readlines()

lines_count = len(m)

REPEAT_COUNT = 200


def replicate(line):
    return line.strip() * REPEAT_COUNT


m = list(map(replicate, m))


def at(x, y):
    return m[y][x]


def how_many_trees(dx, dy):
    pos = (0, 0)

    trees = 0

    while pos[1] < lines_count:
        if at(*pos) == "#":
            trees += 1

        pos = (pos[0] + dx, pos[1] + dy)

    return trees


res = 1

for (dx, dy) in (
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2),
):
    res *= how_many_trees(dx, dy)

print(res)

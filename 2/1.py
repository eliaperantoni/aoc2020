import re

lines = open("input.txt").readlines()


def structify(line):
    m = re.match(r"(\d+)-(\d+) (\w): (\w+)", line)
    return {
        "min": int(m.group(1)),
        "max": int(m.group(2)),
        "letter": m.group(3),
        "string": m.group(4),
    }


passwords = list(map(structify, lines))

correct = 0


def cnt(target, s):
    cnt = 0
    for c in s:
        if c == target:
            cnt += 1
    return cnt


for password in passwords:
    got = cnt(password["letter"], password["string"])
    if password["min"] <= got <= password["max"]:
        correct += 1

print(correct)

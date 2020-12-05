import re

lines = open("input.txt").readlines()


def structify(line):
    m = re.match(r"(\d+)-(\d+) (\w): (\w+)", line)
    return {
        "a": int(m.group(1)),
        "b": int(m.group(2)),
        "letter": m.group(3),
        "string": m.group(4),
    }


passwords = list(map(structify, lines))

correct = 0


def is_ok(password):
    ok = False
    for (i, c) in enumerate(password["string"]):
        if c == password["letter"] and (i + 1 == password["a"] or i + 1 == password["b"]):
            if ok:
                return False
            else:
                ok = True
    return ok


for password in passwords:
    if is_ok(password):
        correct += 1

print(correct)

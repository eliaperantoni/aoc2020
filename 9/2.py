import sys

lines = open("input.txt").readlines()
lines = map(str.strip, lines)
codes = map(int, lines)
codes = list(codes)

target = -1

for i in range(25, len(codes)):
    code = codes[i]
    window = codes[i - 25:i]

    ok = False

    for a in window:
        if (code - a) in [b for b in window if b != a]:
            ok = True
            break

    if not ok:
        target = code
        break

for i in range(len(codes)):
    for j in range(i + 2, len(codes)):
        window = codes[i:j]
        if sum(window) == target:
            print(max(window) + min(window))
            sys.exit(0)

lines = open("input.txt").readlines()
lines = map(str.strip, lines)
codes = map(int, lines)
codes = list(codes)

for i in range(25, len(codes)):
    code = codes[i]
    window = codes[i-25:i]

    ok = False

    for a in window:
        if (code - a) in [b for b in window if b != a]:
            ok = True
            break

    if not ok:
        print(code)
        break

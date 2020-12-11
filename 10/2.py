def paths(adapts, i, memoiz):
    if memoiz[i] != -1:
        return memoiz[i]

    if i == len(adapts) - 1:
        return 1

    res = 0
    for j in range(i + 1, min(i + 4, len(adapts))):
        if adapts[j] - adapts[i] <= 3:
            res += paths(adapts, j, memoiz)

    memoiz[i] = res

    return res


def main():
    lines = open("input.txt").readlines()
    lines = map(str.strip, lines)

    adapts = map(int, lines)
    adapts = list(adapts)

    adapts = [0] + adapts + [max(adapts) + 3]

    adapts.sort()

    memoiz = [-1] * len(adapts)

    print(paths(adapts, 0, memoiz))


if __name__ == '__main__':
    main()

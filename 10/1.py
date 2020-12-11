from collections import Counter

lines = open("input.txt").readlines()
lines = map(str.strip, lines)

adapts = map(int, lines)
adapts = list(adapts)

adapts = [0] + adapts + [max(adapts) + 3]

adapts.sort()

diffs = []

for i in range(len(adapts) - 1):
    diffs.append(adapts[i+1] - adapts[i])

counts = Counter(diffs)
print(counts[1] * counts[3])

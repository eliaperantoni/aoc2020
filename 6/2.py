text = open("input.txt").read()
groups = text.split("\n\n")
groups = map(lambda form: form.splitlines(), groups)


def count_intersection_letters(group):
    letters = {}
    for person in group:
        for c in person:
            if c in letters:
                letters[c].append(None)
            else:
                letters[c] = [None]

    return len(list(filter(lambda entry: len(entry[1]) == len(group), letters.items())))


groups = map(count_intersection_letters, groups)
print(sum(groups))

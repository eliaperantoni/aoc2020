text = open("input.txt").read()
groups = text.split("\n\n")
groups = map(lambda form: form.splitlines(), groups)


def count_unique_letters(group):
    letters = {}
    for person in group:
        for c in person:
            letters[c] = None
    return len(letters)


groups = map(count_unique_letters, groups)
print(sum(groups))

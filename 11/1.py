import copy

height = None
width = None


def count_occ(seats):
    count = 0

    for i in range(height):
        for j in range(width):
            if seats[i][j] == '#':
                count += 1

    return count


def adj_occ(seats, i, j):
    count = 0

    for ii in range(max(0, i - 1), min(height, i + 2)):
        for jj in range(max(0, j - 1), min(width, j + 2)):
            if (ii != i or jj != j) and seats[ii][jj] == '#':
                count += 1

    return count


def display(seats):
    for row in seats:
        print(''.join(row))


def main():
    seats = open('input.txt').readlines()
    seats = map(str.strip, seats)
    seats = map(list, seats)
    seats = list(seats)

    global height, width

    height = len(seats)
    width = len(seats[0])

    first = True
    prev = copy.deepcopy(seats)

    while first or seats != prev:
        prev = copy.deepcopy(seats)
        first = False

        for i in range(height):
            for j in range(width):
                if prev[i][j] == 'L' and adj_occ(prev, i, j) == 0:
                    seats[i][j] = '#'
                elif prev[i][j] == '#' and adj_occ(prev, i, j) >= 4:
                    seats[i][j] = 'L'

    print(count_occ(seats))


if __name__ == '__main__':
    main()

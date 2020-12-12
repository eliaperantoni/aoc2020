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


def vis_occ(seats, i, j):
    count = 0

    for di in range(-1, 2):
        for dj in range(-1, 2):
            if (di, dj) == (0, 0):
                continue

            pos = (i, j)
            while True:
                pos = (pos[0] + di, pos[1] + dj)

                if not (0 <= pos[0] < height and 0 <= pos[1] < width):
                    break

                c = seats[pos[0]][pos[1]]

                if c == '#':
                    count += 1
                    break
                elif c == 'L':
                    break

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
                if prev[i][j] == 'L' and vis_occ(prev, i, j) == 0:
                    seats[i][j] = '#'
                elif prev[i][j] == '#' and vis_occ(prev, i, j) >= 5:
                    seats[i][j] = 'L'

    print(count_occ(seats))


if __name__ == '__main__':
    main()

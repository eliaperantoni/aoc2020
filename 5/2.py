import itertools

seats = open("input.txt").readlines()

ROWS = 128
COLS = 8

seats = map(str.strip, seats)
seats = map(lambda seat: (seat[:7], seat[7:]), seats)
seats = list(seats)


def seat_row(seat):
    row = (0, ROWS - 1)

    for step in seat[0]:
        if step == "F":
            row = (row[0], row[0] + (row[1] - row[0] + 1) / 2 - 1)
        else:
            row = (row[1] - (row[1] - row[0] + 1) / 2 + 1, row[1])

    return int(row[0])


def seat_col(seat):
    col = (0, COLS - 1)

    for step in seat[1]:
        if step == "L":
            col = (col[0], col[0] + (col[1] - col[0] + 1) / 2 - 1)
        else:
            col = (col[1] - (col[1] - col[0] + 1) / 2 + 1, col[1])

    return int(col[0])


def seat_id(seat):
    return seat_row(seat) * 8 + seat_col(seat)


seats_ids = list(map(seat_id, seats))

missing_seats = []

for (row, col) in itertools.product(range(1, ROWS - 1), range(0, COLS)):
    this_seat_id = row * 8 + col
    if this_seat_id not in seats_ids and this_seat_id - 1 in seats_ids and this_seat_id + 1 in seats_ids:
        print(this_seat_id)

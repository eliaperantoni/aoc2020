card_offsets = {
    'E': (1, 0),
    'N': (0, 1),
    'W': (-1, 0),
    'S': (0, -1),
}


def move(pos, offset, magnitude):
    return pos[0] + offset[0] * magnitude, pos[1] + offset[1] * magnitude


def main():
    cmds = open("input.txt").readlines()
    cmds = map(str.strip, cmds)
    cmds = map(lambda line: (line[0], int(line[1:])), cmds)
    cmds = list(cmds)

    ship_pos = (0, 0)
    wayp_pos = (10, 1)

    for cmd in cmds:
        if cmd[0] == 'F':
            ship_pos = move(ship_pos, wayp_pos, cmd[1])
        elif cmd[0] == 'L':
            for i in range(cmd[1] // 90):
                # Thank you linear algebra
                wayp_pos = (-wayp_pos[1], wayp_pos[0])
        elif cmd[0] == 'R':
            for i in range(cmd[1] // 90):
                # Thank you again <3
                wayp_pos = (wayp_pos[1], -wayp_pos[0])
        elif cmd[0] in ['E', 'N', 'W', 'S']:
            wayp_pos = move(wayp_pos, card_offsets[cmd[0]], cmd[1])

    print(abs(ship_pos[0]) + abs(ship_pos[1]))


if __name__ == '__main__':
    main()

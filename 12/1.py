card_offsets = {
    'E': (1, 0),
    'N': (0, 1),
    'W': (-1, 0),
    'S': (0, -1),
}

dir_offsets = {
    0: (1, 0),
    90: (0, 1),
    180: (-1, 0),
    270: (0, -1),
}


def move(pos, offset, magnitude):
    return pos[0] + offset[0] * magnitude, pos[1] + offset[1] * magnitude


def main():
    cmds = open("input.txt").readlines()
    cmds = map(str.strip, cmds)
    cmds = map(lambda line: (line[0], int(line[1:])), cmds)
    cmds = list(cmds)

    pos = (0, 0)
    dir = 0

    for cmd in cmds:
        if cmd[0] in ['E', 'N', 'W', 'S']:
            offset = card_offsets[cmd[0]]
            pos = move(pos, offset, cmd[1])
        elif cmd[0] in ['F']:
            offset = dir_offsets[dir]
            pos = move(pos, offset, cmd[1])
        elif cmd[0] == 'L':
            dir = (dir + cmd[1]) % 360
        else:
            dir = (dir - cmd[1]) % 360

    print(abs(pos[0]) + abs(pos[1]))


if __name__ == '__main__':
    main()

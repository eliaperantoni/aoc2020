import copy

lines = map(str.strip, open("input.txt").readlines())
cmds = map(lambda line: [line[:3], int(line[4:]), False], lines)
cmds = list(cmds)


def execute(cmds):
    acc = 0
    ip = 0

    while ip < len(cmds):
        cmd = cmds[ip]

        if cmd[2]:
            return None

        cmd[2] = True

        if cmd[0] == "jmp":
            ip += cmd[1]
            continue
        elif cmd[0] == "acc":
            acc += cmd[1]
        ip += 1

    return acc


for i in range(len(cmds)):
    cmds_copy = copy.deepcopy(cmds)
    if cmds_copy[i][0] == "jmp":
        cmds_copy[i][0] = "nop"
    elif cmds_copy[i][0] == "nop":
        cmds_copy[i][0] = "jmp"
    else:
        continue

    res = execute(cmds_copy)
    if res is not None:
        print(res)

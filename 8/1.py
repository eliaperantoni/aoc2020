lines = map(str.strip, open("input.txt").readlines())
cmds = map(lambda line: [line[:3], int(line[4:]), False], lines)
cmds = list(cmds)

acc = 0
ip = 0

while True:
    cmd = cmds[ip]

    if cmd[2]:
        print(acc)
        break

    cmd[2] = True

    if cmd[0] == "jmp":
        ip += cmd[1]
        continue
    elif cmd[0] == "acc":
        acc += cmd[1]
    ip += 1

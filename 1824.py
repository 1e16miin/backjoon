def episode(x, y, dx, dy, mem, flag, cnt):
    cur = commands[y][x]
    # print(cur)
    if cnt > 500:
        return print("NO")
    if cur == "@":
        return print("YES")
    elif cur.isdigit():
        mem = int(cur)
    elif cur == "<":
        dx, dy = direction[0]
    elif cur == ">":
        dx, dy = direction[3]
    elif cur == "^":
        dx, dy = direction[2]
    elif cur == "_":
        if mem != 0:
            dx, dy = direction[0]
        else:
            dx, dy = direction[3]
    elif cur == "|":
        if mem != 0:
            dx, dy = direction[2]
        else:
            dx, dy = direction[1]
    elif cur == ".":
        pass
    elif cur == "+":
        mem += 1
        mem %= 16
    elif cur == "-":
        mem -= 1
        mem %= 16
    elif cur == "?":
        if flag == 0:
            dx, dy = direction[0]
            flag += 1
        elif flag == 1:
            dx, dy = direction[1]
            flag += 1
        elif flag == 2:
            dx, dy = direction[2]
            flag += 1
        elif flag == 3:
            dx, dy = direction[3]
            flag += 1
        else:
            return print("NO")

    else:
        dx, dy = direction[2]

    y += dy
    y %= cols
    x += dx
    x %= rows
    cnt += 1
    episode(x, y, dx, dy, mem, flag, cnt)


T = int(input())

direction = [[-1, 0], [0, -1], [0, 1], [1, 0]]
for test_case in range(1, T+1):
    cols, rows = map(int, input().split())

    commands = [input() for _ in range(cols)]
    print("#" + str(test_case), end=" ")
    episode(0, 0, 1, 0, 0, 0, 0)


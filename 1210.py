for _ in range(1, 11):
    test_case = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    y = 99
    # print(ladder)
    idx = ladder[y].index(2)
    flag = 0
    while y > 0:
        # print(idx)
        if flag == 0:
            y -= 1
            if idx > 0 and ladder[y][idx-1] == 1:
                flag = 1
            elif idx < 99 and ladder[y][idx+1] == 1:
                flag = 2

        else:
            if idx > 0 and flag == 1 and ladder[y][idx-1] == 1:
                idx -= 1

            elif idx < 99 and flag == 2 and ladder[y][idx+1] == 1:
                idx += 1

            else:
                flag = 0

    print("#" + str(test_case)+ " " +str(idx))




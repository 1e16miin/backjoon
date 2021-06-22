for _ in range(1, 11):
    test_case = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]

    result = []
    for i in range(100):
        y = 0
        cnt = 0
        flag = 0
        if ladder[y][i] == 1:
            idx = i
            while True:
                cnt += 1
                if y == 99:
                    break
                if flag == 0:
                    y += 1
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

            result.append([cnt, i])
    answer = sorted(result, key=lambda x: (x[0], -x[1]))

    print("#" + str(test_case)+ " " + str(answer[0][1]))
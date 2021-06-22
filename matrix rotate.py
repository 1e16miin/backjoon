def solution(rows, columns, queries):
    answer = []
    matrix = [[0 for _ in range(columns)] for _ in range(rows)]

    for x in range(rows):
        for y in range(columns):
            matrix[x][y] = y + x * columns + 1

    for t in queries:
        x1, y1, x2, y2 = t
        temp = [matrix[x1-1][y1-1]]
        cnt = 0
        for y in range(y1, y2):
            temp.append(matrix[x1-1][y])
            matrix[x1-1][y] = temp[cnt]
            cnt += 1
        print(temp)
        # print(cnt)
        for x in range(x1, x2):
            temp.append(matrix[x][y2-1])
            matrix[x][y2-1] = temp[cnt]
            cnt += 1
        print(temp)
        # print(cnt)
        for y in range(y2-1, y1-1, -1):
            temp.append(matrix[x2-1][y])
            matrix[x2-1][y] = temp[cnt]
            cnt += 1
        print(temp)
        # print(cnt)
        for x in range(x2-1, x1-1, -1):
            temp.append(matrix[x][y1-1])
            matrix[x][y1-1] = temp[cnt]
            cnt += 1
        print(temp)
        # print(cnt)
        matrix[x1-1][y1-1] = temp[cnt]
        # print(temp)
        answer.append(min(temp))

    return answer


print(solution(3,3,[[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]))
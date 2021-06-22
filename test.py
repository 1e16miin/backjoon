T = int(input())


for test_case in range(1, T+1):
    N = int(input())
    board = [list(map(int, input())) for _ in range(N)]
    dp = [[0 for _ in range(N)] for _ in range(N)]
    # print(board)
    for y in range(N):
        for x in range(N):
            # if x == 0 and y == 0:
            #     pass
            if x == 0 and y > 0:
                dp[y][x] = board[y][x] + dp[y-1][x]
            elif y == 0 and x > 0:
                dp[y][x] = board[y][x] + dp[y][x-1]
            elif x > 0 and y > 0:
                dp[y][x] = min(dp[y][x-1], dp[y-1][x]) + board[y][x]
    # print(dp)
    # print("#"+str(test_case) + " " + str(dp[N-1][N-1]))

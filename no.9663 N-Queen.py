import sys


def dfs(row, col, queens, set_row, set_col):
    if queens == 1:
        print(1)
        return 1
    # temp = set()
    # temp.add(col)
    queens -= 1
    set_row.add(row)
    set_col.add(col)
    for x in number-set_row:
        for y in number-set_col:
            # print(x, y)
            dfs(x, y, queens, set_row, set_col)

    return 0


N = int(sys.stdin.readline())
# graph = {str(i): set(j for j in range(N)) for i in range(N)}
number = set(i for i in range(N))
answer = 0
for i in range(N):
    answer += dfs(0, i, N, set(), set())

print(answer)
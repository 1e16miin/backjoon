import sys
from collections import deque


def prob(cur, days):
    if days == 0:
        return 1 if cur == P else 0

    ret = dp[cur][days]
    if ret > -0.5:
        return ret

    ret = 0
    for to in range(N):
        if matrix[cur][to] != 0:
            ret += prob(to, days - 1) / degree[to]

    dp[cur][days] = ret
    return ret


if __name__ == "__main__":
    T = int(sys.stdin.readline().rstrip())
    answer = ""

    for _ in range(T):
        N, D, P = map(int, sys.stdin.readline().split())
        dp = deque([[-1 for _ in range(D + 1)] for _ in range(N + 1)])
        matrix = [deque(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
        M = int(sys.stdin.readline().rstrip())
        Q = deque(map(int, sys.stdin.readline().strip().split()))
        degree = deque([matrix[i].count(1) for i in range(N)])
        ans = ""
        for destination in Q:
            ans += str(prob(destination, D)) + ' '

        sys.stdout.write(ans)

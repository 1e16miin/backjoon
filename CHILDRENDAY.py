from collections import deque
import sys


def bfs(d, n, m):
    q = deque(d)
    visited = [[-1 for _ in range(len(d))] for _ in range(n)]

    while q:
        here = q.popleft()
        if here >= n + m and (here - m) % n == 0:
            return here

        for i in range(len(d)):
            mod = (here * 10 + d[i]) % n
            if visited[mod][i] == -1:
                visited[mod][i] = mod
                q.append(here * 10 + d[i])

    return "IMPOSSIBLE"


if __name__ == '__main__':
    C = int(sys.stdin.readline())
    for _ in range(C):
        d, n, m = map(str, sys.stdin.readline().strip().split())
        d = list(map(int, d))
        print(d)
        d.sort()
        n = int(n)
        m = int(m)
        print(bfs(d, n, m))
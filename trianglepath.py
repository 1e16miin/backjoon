import sys


class triangle_sum:
    def __init__(self):
        self.cache = [[-1 for _ in range(100)] for _ in range(100)]

    def path_sum(self, y, x):
        if y == n-1:
            return triangle[y][x]
        if self.cache[y][x] != -1:
            return self.cache[y][x]

        self.cache[y][x] = max(self.path_sum(y + 1, x), self.path_sum(y + 1, x + 1)) + triangle[y][x]
        return self.cache[y][x]


T = int(sys.stdin.readline())

answer = []
for i in range(T):
    ts = triangle_sum()
    n = int(sys.stdin.readline())
    triangle = []
    for _ in range(n):
        triangle.append(list(map(int, sys.stdin.readline().split())))
    answer.append(ts.path_sum(0, 0))

print(answer)
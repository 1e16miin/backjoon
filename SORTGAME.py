from collections import deque
import sys


def pre_calc(n):
    perm = '01234567'
    perm = perm[:n]
    q = deque()
    q.append(perm)
    to_sort[perm] = 0
    while q:
        here = q.popleft()
        cost = to_sort[here]
        for i in range(n):
            for j in range(i+2, n+1):
                if i == 0:
                    partial = reversed(here[:j+1])
                    temp = ''.join(partial) + here[j+1:]
                else:
                    temp = here[:i] + here[j:i-1:-1] + here[j+1:]
                if temp not in to_sort:
                    to_sort[temp] = cost + 1
                    q.append(temp)


def solve(perm):
    n = len(perm)
    fixed = ""
    for i in range(n):
        smaller = 0
        for j in range(n):
            if perm[j] < perm[i]:
                smaller += 1
        fixed += str(smaller)
    return to_sort[fixed]


if __name__ == '__main__':
    C = int(sys.stdin.readline())
    for _ in range(C):
        N = int(sys.stdin.readline())
        to_sort = dict()
        seq = list(map(int, sys.stdin.readline().strip().split()))
        pre_calc(N)
        print(solve(seq))

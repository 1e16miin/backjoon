import sys
# import math
from _collections import deque


def JLIS(idx1, idx2):
    res = subseq[idx1+1][idx2+1]
    if res != -1:
        return res
    res = 0
    a = (min_val if idx1 == -1 else seq1[idx1])
    b = (min_val if idx2 == -1 else seq2[idx2])
    max_element = max(a, b)
    for idx in range(idx1 + 1, n):
        if max_element < seq1[idx]:
            res = max(res, JLIS(idx, idx2) + 1)

    for idx in range(idx2 + 1, m):
        if max_element < seq2[idx]:
            res = max(res, JLIS(idx1, idx) + 1)

    subseq[idx1][idx2] = res
    return res


min_val = float('-inf')
T = int(sys.stdin.readline())
for _ in range(T):
    n, m = map(int, sys.stdin.readline().split())

    seq1 = deque(map(int, sys.stdin.readline().split()))
    seq2 = deque(map(int, sys.stdin.readline().split()))

    subseq = [[-1 for _ in range(101)] for _ in range(101)]
    print(JLIS(-1, -1))
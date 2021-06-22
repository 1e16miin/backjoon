import sys


def LIS(idx):
    res = subseq[idx]
    if res != -1:
        return res
    res = 1
    for pivot in range(idx + 1, n):
        if seq[idx] < seq[pivot]:
            res = max(res, LIS(pivot) + 1)

    subseq[idx] = res
    return res


n = int(sys.stdin.readline())
seq = list(map(int, sys.stdin.readline().split()))
subseq = [-1 for _ in range(n)]
result = 0
for i in range(n):
    result = max(result, LIS(i))
print(result)
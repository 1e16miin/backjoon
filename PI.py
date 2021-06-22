import sys


def level(start, fin):
    sub_seq = seq[start:fin]
    if sub_seq == [sub_seq[0] for _ in range(len(sub_seq))]:
        return 1

    progressive = True
    for i in range(len(sub_seq) - 1):
        if (sub_seq[i + 1] - sub_seq[i]) != (sub_seq[1] - sub_seq[0]):
            progressive = False

    if progressive and abs(sub_seq[1] - sub_seq[0]) == 1:
        return 2

    alternative = True
    for j in range(len(sub_seq)):
        if sub_seq[j] != sub_seq[j % 2]:
            alternative = False

    if alternative:
        return 4

    if progressive:
        return 5

    return 10


def memorize(begin):
    if begin == len(seq):
        return 0

    ret = dp[begin]
    if ret != -1:
        return ret

    ret = INF
    for L in range(3, 6):
        if begin + L <= len(seq):
            ret = min(ret, memorize(begin + L) + level(begin, begin + L))

    dp[begin] = ret
    return ret


if __name__ == "__main__":
    T = int(sys.stdin.readline().rstrip())
    INF = float('inf')
    sys.setrecursionlimit(10**8)
    answer = [0 for _ in range(T)]
    for tc in range(T):
        seq = list(map(int, list(sys.stdin.readline().strip())))
        dp = [-1 for _ in range(10002)]
        answer[tc] = memorize(0)

    for i in range(T):
        print(answer[i])
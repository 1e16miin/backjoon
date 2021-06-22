import sys
import math


def quantize(start, parts):
    if start == n:
        return 0

    if parts == 0:
        return INF

    ret = dp[start][parts]

    if ret != -1:
        return ret

    ret = INF
    for i in range(1, n - start + 1):
        ret = min(ret, variance(start, i) + quantize(start+i, parts-1))

    dp[start][parts] = ret
    return ret


def variance(start, size):
    sub_seq = seq[start:start+size]
    reverse_sub_seq = list(reversed(sub_seq))
    # print(reverse_sub_seq)
    p_sum = 0
    for i in range(size):
        p_sum += (sub_seq[i] + reverse_sub_seq[i])

    p_sum /= 2
    avg = int(p_sum/size + 0.5)
    var = size*math.pow(avg, 2) - 2*avg*p_sum
    for i in range(size):
        var += math.pow(sub_seq[i], 2)

    return var


if __name__ == "__main__":
    T = int(sys.stdin.readline().rstrip())
    sys.setrecursionlimit(10**8)
    INF = float('inf')
    answer = ""
    for tc in range(T):
        n, s = map(int, sys.stdin.readline().strip().split())
        seq = list(map(int, sys.stdin.readline().strip().split()))
        seq.sort()
        dp = [[-1 for _ in range(11)] for _ in range(101)]
        answer += str(quantize(0, s)) + '\n'
    print(answer)
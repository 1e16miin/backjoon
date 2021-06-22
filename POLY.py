import sys


def poly(n, first):
    if n == first:
        return 1

    ret = dp[n][first]

    if ret != -1:
        return ret

    ret = 0
    for second in range(1, n-first+1):
        head = first + second - 1
        head *= poly(n-first, second)
        head %= MOD
        ret += head
        ret %= MOD

    dp[n][first] = ret
    return ret


if __name__ == "__main__":
    T = int(sys.stdin.readline().rstrip())
    MOD = int(1e7)
    answer = ""
    dp = [[-1 for _ in range(102)] for _ in range(102)]
    for _ in range(T):
        N = int(sys.stdin.readline().rstrip())
        res = 0
        for i in range(1, N+1):
            res += poly(N, i)
            res %= MOD
        answer += str(res) + '\n'
    print(answer)
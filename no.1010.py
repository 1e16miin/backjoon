def factorial(n):
    res = 1
    for i in range(n):
        res *= n-i

    return res


T = int(input())

for i in range(T):
    N, M = map(int, input().split())
    if N == 0 or M == 0:
        print(0)

    m = factorial(M)
    n = factorial(N)
    m_n = factorial(M-N)

    result = int(m//n//m_n)
    print(result)
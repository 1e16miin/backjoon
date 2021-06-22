n_elements = int(input())

elements = sorted(list(map(int, input().split())))

N = int(input())

lower = 0

if N in elements:
    print(0)

else:
    for i in elements:
        if i < N:
            lower = i
        else:
            upper = i
            break

    num = (N - lower - 1) * (upper - N - 1) + upper - lower - 2
    print(num)
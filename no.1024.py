import sys

N, L = map(int, sys.stdin.readline().split())

flag = 0

for i in range(L, 101):
    temp = N - i*(i+1)//2
    if temp % i == 0:
        j = temp // i + 1
        if j >= 0:
            flag = 1
            for k in range(j, j+i):
                sys.stdout.write(str(k) + ' ')
            break

if flag == 0:
    print(-1)
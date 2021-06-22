from _collections import deque

dq = deque()

for i in range(10, 100):
    q = i // 10
    r = i % 10
    if q > r:
        dq.append(i)

N = int(input())

digit = 0
balance = 10
temp = 0
if N < 10:
    print(N)
elif N > 294:
    print(-1)
else:
    temp = N - 9
    for i in range(1, 10):
        if temp < 5*(i+1)*(i+2) - (i+2)*(i+1)*(2*i+3)//6:
            digit = i
            break

    for i in range(1, digit):
        for j in range(balance - i):
            loc = 
            dq.append(dq)

    print(digit)
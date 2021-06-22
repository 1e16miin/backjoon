N = int(input())

result = N
temp = 0
new = 0
cnt = 0
q = 0
r = 0
while True:
    cnt += 1
    q = N // 10
    r = N % 10
    temp = q + r
    new = r * 10 + temp % 10
    N = new
    if new == result:
        break

print(cnt)
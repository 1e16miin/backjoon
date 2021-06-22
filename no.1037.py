n_div = int(input())

divs = list(map(int, input().split()))

min = 100001
max = 1

for i in range(n_div):
    if divs[i] > max:
        max = divs[i]
    if divs[i] < min:
        min = divs[i]

N = min*max

print(N)
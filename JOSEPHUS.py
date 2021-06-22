import sys
from collections import deque


T = int(sys.stdin.readline())
for _ in range(T):
    N, K = map(int, sys.stdin.readline().split())
    people = deque([i + 1 for i in range(N)])
    while N > 2:
        people.popleft()
        N -= 1
        people.rotate(-(K-1))

    people = sorted(people)
    print(*people)
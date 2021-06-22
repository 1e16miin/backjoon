import sys
from collections import deque


T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    heights = list(map(int, sys.stdin.readline().strip().split()))
    heights.append(0)
    N += 1
    stack = deque([])
    ret = 0
    for i in range(N):
        while stack and heights[stack[-1]] >= heights[i]:
            j = stack.pop()
            if not stack:
                width = i
            else:
                width = i - stack[-1] - 1
            ret = max(ret, heights[j]*width)
        stack.append(i)

    sys.stdout.write(str(ret)+'\n')
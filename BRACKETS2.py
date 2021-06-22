import sys
from collections import deque


bracket = {'[': ']', '{': '}', '(': ')'}
T = int(sys.stdin.readline())
for _ in range(T):
    stack = deque([])
    brackets = str(sys.stdin.readline().strip())
    match = True
    for i in range(len(brackets)):
        sign = brackets[i]
        if sign in bracket.keys():
            stack.append(sign)

        else:
            if not stack:
                match = False
                break
            elif bracket[stack[-1]] != sign:
                match = False
                break
            stack.pop()

    if stack:
        match = False

    if not match:
        print("NO")
    else:
        print("YES")
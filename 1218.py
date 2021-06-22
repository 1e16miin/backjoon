from collections import deque


bracket = {"}": "{", "]": "[" , ")": "(", ">": "<"}
for test_case in range(1,11):
    N = int(input())
    seq = deque(input())
    stack = [seq.popleft()]
    answer = 1
    while stack:
        if not seq:
            answer = 0
            break
        cur = seq.popleft()
        if cur in bracket.values():
            stack.append(cur)
        else:
            if bracket[cur] == stack[-1]:
                stack.pop()
            else:
                stack.append(cur)

    print("#" + str(test_case) + " " + str(answer))
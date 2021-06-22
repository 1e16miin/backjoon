import sys
# from collections import deque


def post_order(order1, order2):
    n = len(order1)
    if not order1:
        return

    root = order1[0]
    l = order2.index(root)
    post_order(order1[1: l+1], order2[0: l])
    post_order(order1[l+1: n], order2[l+1: n])

    sys.stdout.write(str(root) + " ")


T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    pre_order = list(map(int, sys.stdin.readline().strip().split()))
    in_order = list(map(int, sys.stdin.readline().strip().split()))
    answer = ""
    post_order(pre_order, in_order)

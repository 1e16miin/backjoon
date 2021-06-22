import sys

A_len = int(input())

A = list(map(int, input().split()))

B = sorted(A)

P = [0 for i in range(A_len)]

for i in range(A_len):
    for j in range(A_len):
        if A[i] == B[j]:
            P[i] = j
            B[j] = -1
            break

for pn in P:
    sys.stdout.write(str(pn)+' ')
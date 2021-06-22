import sys

X, Y = map(int, sys.stdin.readline().split())

Z = int(Y/X *100)

print(Z)
import sys


sys.setrecursionlimit(1000000)


def dfs(cur_x, cur_y, dist):
    visit = set()
    stack = []

    stack.append



for test_case in range(1):
    N = int(input())
    locations = list(map(int, input().split()))
    company_x, company_y = locations[0], locations[1]
    home_x, home_y = locations[2], locations[3]
    xs = [locations[i] for i in range(4, 2*N+4, 2)]
    ys = [locations[i] for i in range(5, 2*N+4, 2)]
    # print(xs)
    visited = []
    # distances = []

    dfs(company_x, company_y, 0)
    # print(distances)

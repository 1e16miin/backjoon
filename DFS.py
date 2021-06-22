import sys
from collections import deque


def dfs(graph, start_node):
    visit = set()
    stack = deque()

    stack.append(start_node)
    while stack:
        node = stack.pop()
        if node not in visit:
            visit.add(node)
            stack.extend(graph[node])

    return frozenset(visit)


def solution(n, computers):
    graph = {node: [] for node in range(n)}

    for i, computer in enumerate(computers):
        for j, conn in enumerate(computer):
            if i != j and conn == 1:
                graph[i].append(j)

    paths = set()
    for node in graph:
        paths.add(dfs(graph, node))

    return paths
    # return len(set(["".join(map(str, path)) for path in paths]))


print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
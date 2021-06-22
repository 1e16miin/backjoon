from collections import deque

adj = []


def bfs(start, dist, parent):
    # dist = [-1 for _ in range(len(adj))]
    # parent = [-1 for _ in range(len(adj))]
    q = deque()
    dist[start] = 0
    parent[start] = start
    q.append(start)

    while q:
        here = q.popleft()
        for i in range(len(adj)):
            there = adj[here][i]
            if dist[there] == -1:
                q.append(there)
                dist[there] = dist[here] + 1
                parent[there] = here
import sys


def make_graph(words):
    graph = [[0 for _ in range(m)] for _ in range(m)]
    for k in range(1, len(words)):
        idx = k - 1
        length = min(len(words[k]), len(words[idx]))
        for j in range(length):
            if words[k][j] != words[idx][j]:
                a = ord(words[idx][j]) - ord('a')
                b = ord(words[k][j]) - ord('a')
                graph[a][b] = 1
                break
    return graph


def dfs(here):
    visited[here] = True
    for there in range(len(adj[here])):
        if adj[here][there] == 1 and visited[there] is False:
            dfs(there)

    order.append(here)


if __name__ == "__main__":
    sys.setrecursionlimit(10**6)
    rl = lambda: sys.stdin.readline().strip()
    T = int(rl())
    for _ in range(T):
        m = 26
        visited = [False for _ in range(m)]
        N = int(rl())
        order = []
        word_list = []
        for _ in range(N):
            temp = rl()
            word_list.append(temp)
        adj = make_graph(word_list)

        for v in range(m):
            if visited[v] is False:
                dfs(v)
        order.reverse()

        for u in range(m):
            for v in range(u + 1, m):
                if adj[order[v]][order[u]]:
                    order = []
                    break

        if len(order) == 0:
            print("INVALID HYPOTHESIS")
        else:
            answer = ""
            for i in range(m):
                answer += chr(order[i]+ord('a'))
            print(answer)

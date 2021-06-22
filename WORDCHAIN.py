from collections import deque
import sys


def make_graph(words):
    for i in range(len(words)):
        a = ord(words[i][0]) - ord('a')
        b = ord(words[i][-1]) - ord('a')
        graph[a][b].append(words[i])
        adj[a][b] += 1
        outdegree[a] += 1
        indegree[b] += 1


#dfs
def get_euler_circuit(here, circuit):
    for there in range(m):
        while adj[here][there] > 0:
            adj[here][there] -= 1
            get_euler_circuit(there, circuit)

    circuit.append(here)


def get_euler_trail_or_circuit():
    circuit = []

    for i in range(m):
        if outdegree[i] == indegree[i] + 1:
            get_euler_circuit(i, circuit)
            return circuit

    for i in range(m):
        if outdegree[i]:
            get_euler_circuit(i, circuit)
            return circuit
    return circuit


def check_euler():
    start = 0
    fin = 0
    for i in range(m):
        delta = outdegree[i] - indegree[i]
        if delta < -1 or delta > 1:
            return False
        if delta == 1:
            start += 1
        if delta == -1:
            fin += 1

    return (start == 1 and fin == 1) or (start == 0 and fin == 0)


def solve(words):
    make_graph(words)
    if not check_euler():
        return "IMPOSSIBLE"

    path = get_euler_trail_or_circuit()
    if len(path) != len(word_list) + 1:
        return "IMPOSSIBLE"

    path.reverse()

    ret = ""
    for i in range(1, len(path)):
        a = path[i - 1]
        b = path[i]
        if ret:
            ret += " "
        ret += graph[a][b].pop()

    return ret


if __name__ == '__main__':
    sys.setrecursionlimit(10**6)
    T = int(sys.stdin.readline())
    for _ in range(T):
        visited = [False for _ in range(26)]
        adj = [[0 for _ in range(26)] for _ in range(26)]
        N = int(sys.stdin.readline())
        graph = [[deque() for _ in range(26)] for _ in range(26)]
        indegree = [0 for _ in range(26)]
        outdegree = [0 for _ in range(26)]
        m = len(adj)
        word_list = [str(sys.stdin.readline().strip()) for _ in range(N)]
        ans = solve(word_list)
        print(ans)
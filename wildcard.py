import sys


class Wildcard:
    def __init__(self):
        self.cache = [[-1 for _ in range(101)] for _ in range(101)]

    def match(self, w, s):
        # ret = self.cache[w][s]
        if self.cache[w][s] != -1:
            return self.cache[w][s]

        while s < len(S) and w < len(W) and (W[w] == "?" or W[w] == S[s]):
            s += 1
            w += 1

        if w == len(W):
            self.cache[w][s] = (s == len(S))
            # self.cache[w][s] = ret
            return int(self.cache[w][s])

        if W[w] == "*":
            for skip in range(0, len(S) - s + 1):
                if self.match(w+1, s+skip):
                    # ret = 1
                    # self.cache[w][s] = ret
                    self.cache[w][s] = 1
                    return self.cache[w][s]

        self.cache[w][s] = 0
        # ret = 0
        # self.cache[w][s] = ret
        return self.cache[w][s]


if __name__ == '__main__':
    T = int(sys.stdin.readline().rstrip())
    answer = []
    for i in range(T):

        W = sys.stdin.readline().rstrip()
        n = int(sys.stdin.readline().rstrip())
        fileNames = []
        res = []
        for _ in range(n):
            fileNames.append(sys.stdin.readline().rstrip())

        for name in fileNames:
            wc = Wildcard()
            S = name
            if wc.match(0, 0) == 1:
                res.append(name)
        res.sort()
        answer.extend(res)
    for file in answer:
        print(file)


# cnt = 0
#
# for name in fileNames:
#     S = name
#     if wc.match(0, 0) == 1:
#         print(name)
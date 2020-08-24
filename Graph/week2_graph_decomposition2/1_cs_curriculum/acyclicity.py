#Uses python3

import sys


def acyclic(adj):
    V = len(adj)
    visit = [False] * V
    while False in visit:
        v = visit.index(False)
        stack = [v]
        while len(stack) > 0:
            s = stack[-1]
            visit[s] = True
            f = 1
            for i in adj[s]:
                if i in stack:
                    return 1
                elif not visit[i]:
                    f = 0
                    visit[i] = True
                    stack.append(i)
                    break
            if f:
                stack.pop()
    return 0


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj))

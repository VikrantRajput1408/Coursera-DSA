#Uses python3


import sys


def reach(adj, x, y):
    flag = 0
    visited = [False for _ in range(len(adj))]
    stack = [x]
    while len(stack) != 0:
        if y in stack:
            flag = 1
            break
        s = stack[-1]
        stack.pop()
        if not visited[s]:
            visited[s] = True
        for node in adj[s]:
            if not visited[node]:
                stack.append(node)
    return flag


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    x, y = data[2 * m:]
    adj = [[] for _ in range(n)]
    x, y = x - 1, y - 1
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(reach(adj, x, y))

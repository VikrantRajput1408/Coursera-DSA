#Uses python3

import sys


def number_of_components(adj):
    result = 0
    #write your code here
    visited = [False for _ in range(len(adj))]
    while False in visited:
        stack = [visited.index(False)]
        result += 1
        while len(stack) != 0:
            s = stack[-1]
            stack.pop()
            if not visited[s]:
                visited[s] = True
            for node in adj[s]:
                if not visited[node]:
                    stack.append(node)
    return result


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(number_of_components(adj))

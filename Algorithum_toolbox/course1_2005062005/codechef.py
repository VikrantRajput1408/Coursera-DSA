
def solve():
    N, P = map(int, input().split())
    h_N = N//2
    mat = [[1, 1, 1, N, N],
           [1, 1, 1, h_N, h_N],
           [1, 1, h_N+1, h_N, N],
           [1, h_N+1, 1, N, h_N],
           [1, h_N+1, h_N+1, N, N]]
    pat = []
    for i in range(5):
        print(*mat[i])
        pat.append(int(input()))
    ans = [[0 for _ in range(N)] for _ in range(N)]
    if sum(pat) // 2 == pat[0]:
        for i in range(1,len(pat)):
            x_min, y_min, x_max, y_max = mat[i][1:]
            x_min -= 1
            y_min -= 1
            x, y = x_min, y_min
            for j in range(pat[i]):
                ans[x][y] = 1
                if x < (x_max - 1):
                    x += 1
                else:
                    y += 1
                    x = x_min
    print(2)
    for k in range(N):
        print(*ans[k])
    X = int(input())


if __name__ == '__main__':
    try:
        t = int(input())
        for _ in range(t):
            solve()
    except:
        pass
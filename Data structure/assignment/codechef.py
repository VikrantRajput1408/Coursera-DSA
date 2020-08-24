def solve():
    N = int(input())
    arr = []
    for _ in range(N):
        arr.append(int(input()))
    arr.sort()
    max = 0
    for i in arr:
        if i*N > max:
            max = i*N
        N-=1
    print(max)


if __name__ == "__main__":
    try:
        solve()
    except:
        pass
# Uses python3
import sys


def get_change(m):
    coin = [1, 3, 4]
    table = [sys.maxsize] * (m+1)
    table[0] = 0
    for i in range(1, m + 1):
        for j in coin:
            if j <= i:
                res = table[i - j]
                if res != sys.maxsize and res + 1 < table[i]:
                    table[i] = res + 1
    return table[m]


if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))

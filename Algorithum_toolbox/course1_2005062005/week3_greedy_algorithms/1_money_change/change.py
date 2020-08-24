# Uses python3
import sys


def get_change(m):
    coins = [10, 5, 1]
    no_of_coin = 0
    for i in coins:
        no_of_coin += m // i
        m = m % i
    return no_of_coin


if __name__ == '__main__':
    input = sys.stdin.read()
    m = int(input)
    print(get_change(m))
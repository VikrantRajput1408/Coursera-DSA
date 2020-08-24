# Uses python3
import sys


def lcm_naive_2(a, b):
    if b == 0:
        return a
    else:
        return lcm_naive_2(b, a % b)


if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print((a * b) //(lcm_naive_2(a, b)))
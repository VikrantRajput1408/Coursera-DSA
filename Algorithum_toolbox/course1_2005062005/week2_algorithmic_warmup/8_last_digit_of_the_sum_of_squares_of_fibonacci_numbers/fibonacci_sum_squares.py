# Uses python3
from sys import stdin
import numpy

def fibonacci_sum_squares_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current * current

    return sum % 10

if __name__ == '__main__':
    # input = stdin.read()
    n = int(input())
    n = n % 60
    print(fibonacci_sum_squares_naive(n))

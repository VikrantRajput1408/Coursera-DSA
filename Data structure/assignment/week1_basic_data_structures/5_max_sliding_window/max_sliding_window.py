# python3
from collections import deque


def max_sliding_window_naive(sequence, m):
    maximums = []
    for i in range(len(sequence) - m + 1):
        maximums.append(max(sequence[i:i + m]))
    return maximums


def max_sliding_window(arr, n, k):
    Qi = deque()
    for i in range(k):
        while Qi and arr[i] >= arr[Qi[-1]]:
            Qi.pop()
        Qi.append(i)
    for i in range(k, n):
        print(str(arr[Qi[0]]) + " ", end="")
        while Qi and Qi[0] <= i - k:
            Qi.popleft()
        while Qi and arr[i] >= arr[Qi[-1]]:
            Qi.pop()
        Qi.append(i)
    print(str(arr[Qi[0]]))


if __name__ == '__main__':
    n = int(input())
    input_sequence = [int(i) for i in input().split()]
    assert len(input_sequence) == n
    window_size = int(input())
    max_sliding_window(input_sequence, len(input_sequence),window_size)


# Uses python3
import sys
import random


def partition3(a, l, r):
    #write your code here
    if r - l <= 1:
        if a[r] < a[l]:
            a[r], a[l] = a[l], a[r]
        return l, r
    x = a[r]
    j = l
    while j <= r:
        if a[j] < x:
            a[l], a[j] = a[j], a[l]
            l += 1
            j += 1
        elif a[j] == x:
            j += 1
        else:
            a[j], a[r] = a[r], a[j]
            r -= 1
    return (l-1), j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    i, j = partition3(a, l, r)
    randomized_quick_sort(a, l, i)
    randomized_quick_sort(a, j, r)


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')

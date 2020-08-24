import sys


def largest_number(a):
    ext = []
    length = len(max(a)) + 1
    for i in a:
        temp = i * length
        ext.append([temp[:length], i])
    ext.sort(reverse=True)
    res = ""
    for x in ext:
        res += x[1]
    return res


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(str, input.split()))
    a = data[1:]
    print(largest_number(a))

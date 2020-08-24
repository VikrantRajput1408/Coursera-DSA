#python3
import sys


if __name__ == '__main__':
    stack = [None]*400000
    top = -1
    maximum = [0]*400000
    maxi = 0
    num_queries = int(sys.stdin.readline())
    for _ in range(num_queries):
        query = sys.stdin.readline().split()
        if query[0] == "push":
            top += 1
            stack[top] = int(query[1])
            if int(query[1]) > maxi:
                maxi = int(query[1])
            maximum[top] = maxi
        elif query[0] == "pop":
            maxi = maximum[top-1]
            stack[top] = None
            top -= 1

        elif query[0] == "max":
            assert top != -1
            print(maximum[top])
        else:
            assert 0

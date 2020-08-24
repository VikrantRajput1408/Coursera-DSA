# Uses python3
import sys


def optimal_weight(W,w):
    items = [0] + w
    Weight_matrix = [ [0]*(W+1) for _ in range(len(items))]
    for i in range(1,len(items)):
        for j in range(1,(W+1)):
            if j - items[i] < 0:
                Weight_matrix[i][j] = Weight_matrix[i-1][j]
            else:
                Weight_matrix[i][j] = max(Weight_matrix[i-1][j], (Weight_matrix[i-1][j-items[i]]+items[i]))

    return Weight_matrix[-1][-1]


if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))

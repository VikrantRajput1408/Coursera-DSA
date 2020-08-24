# Uses python3
import sys


class ItemValue:
    def __init__(self, wt, val, ind):
        self.wt = wt
        self.val = val
        self.ind = ind
        self.cost = val / wt

    def __lt__(self, other):
        return self.cost < other.cost


def get_optimal_value(capacity, weights, values):
    vbw = []
    for i in range(len(weights)):
        vbw.append(ItemValue(weights[i], values[i], i))
    vbw.sort(reverse=True)
    value = 0
    for i in vbw:
        curWt = int(i.wt)
        curVal = int(i.val)
        if capacity - curWt >= 0:
            capacity -= curWt
            value += curVal
        else:
            fraction = capacity / curWt
            value += curVal * fraction
            capacity = capacity - (curWt * fraction)
            break
    return value


if __name__ == "__main__":
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.4f}".format(opt_value))

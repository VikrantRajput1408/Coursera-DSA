# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []
    #write your code here
    segments.sort(key=lambda x: x[0])
    for s in segments:
        points.append(s.start)
        points.append(s.end)
    i, j = 0, 1
    N = len(segments)
    while N != 0 and i < (len(points) - 2):
        if points[j] >= points[i+2]:
            temp_i = points[i]
            temp_j = points[j]
            points.remove(points[i])
            points.remove(points[i])
            points[i] = max(temp_i, points[i])
            points[j] = min(temp_j, points[j])
        else:
            i += 2
            j += 2
        N -= 1
    points = points[::2]
    return points


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)

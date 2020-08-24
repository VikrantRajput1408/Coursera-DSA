# python3
import sys


def compute_min_refills(distance, tank, stops):
    i = 0
    refill = 0
    home = 0
    while (home+tank) < distance:
        if i > 0 and (stops[i] - stops[i-1]) > tank:
            return -1
        while i < len(stops)-1 and stops[i] <= (home + tank):
            i += 1
        else:
            refill += 1
            home = stops[i-1]
    return refill


if __name__ == '__main__':
    input = sys.stdin.read()
    d, m, _, *stops = map(int, input.split())
    stops.append(d)
    print(compute_min_refills(d, m, stops))

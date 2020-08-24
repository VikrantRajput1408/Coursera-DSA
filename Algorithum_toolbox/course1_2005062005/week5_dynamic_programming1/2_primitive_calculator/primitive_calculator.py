# Uses python3
import sys


def optimal_sequence(n):
    sequence = []
    while n >= 1:
        sequence.append(n)
        if n % 3 == 0:
            n = n // 3
        elif n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
    return reversed(sequence)


def optimal_sequence_2(n):
    sequence_of_seq = [0] * (n+1)
    sequence_of_seq[0] = [0, ]
    sequence_of_seq[1] = [1, ]
    for i in range(2, n+1):
        if i % 3 == 0 and i % 2 == 0:
            res = min(list(sequence_of_seq[i//3]), list(sequence_of_seq[i//2]), list(sequence_of_seq[i - 1]), key=lambda x: len(x))
            res.append(i)
        elif i % 3 == 0:
            res = min(list(sequence_of_seq[i//3]), list(sequence_of_seq[i - 1]), key=lambda x: len(x))
            res.append(i)

        elif i % 2 == 0:
            res = min(list(sequence_of_seq[i//2]), list(sequence_of_seq[i - 1]), key=lambda x: len(x))
            res.append(i)
        else:
            res = list(sequence_of_seq[i - 1])
            res.append(i)
        sequence_of_seq[i] = res
    return sequence_of_seq[n]


input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence_2(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
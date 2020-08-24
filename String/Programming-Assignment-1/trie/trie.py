# Uses python3
import sys


class Trie:

    def __init__(self):
        self.tree = {0: {}}
        self.patterns = []
        self.max_index = 0

    def read(self):
        n = int(input())

        for _ in range(n):
            self.patterns.append(input())

    def build_trie(self):

        for pattern in self.patterns:
            node = 0

            for letter in pattern:
                if letter not in self.tree[node]:
                    self.max_index += 1
                    self.tree[node][letter] = self.max_index
                    self.tree[self.max_index] = {}

                node = self.tree[node][letter]

        return self.tree

    def print_trie(self):
        for node in self.tree:
            for letter in self.tree[node]:
                print('{}->{}:{}'.format(node, self.tree[node][letter], letter))


if __name__ == '__main__':
    trie = Trie()
    trie.read()
    trie.build_trie()
    trie.print_trie()

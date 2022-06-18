import collections
from typing import List
import pprint


Trie = lambda: collections.defaultdict(Trie)
WEIGHT = False


class WordFilter:
    def __init__(self, words: List[str]):
        self.trie = Trie()

        for weight, word in enumerate(words):
            word += '#'

            for i in range(len(word)):
                cur = self.trie
                cur[WEIGHT] = weight

                # print(f'i: {i}, word[i]: {word[i]}')

                # -1 because we don't need to visit # twice
                for j in range(i, 2 * len(word) - 1):

                    # print(f'  j: {j}, word[j % len(word)]: {word[j % len(word)]}')

                    # j exceeds length of word, but j % len(word) wraps it
                    cur = cur[word[j % len(word)]]
                    cur[WEIGHT] = weight

    def f(self, prefix: str, suffix: str) -> int:
        cur = self.trie
        for letter in suffix + '#' + prefix:
            if letter not in cur:
                return -1
            cur = cur[letter]

        # I don't know why it's guaranteed to have the max index
        return cur[WEIGHT]


class WordFilter1:
    def __init__(self, words: List[str]):
        self.trie1 = Trie()  # prefix
        self.trie2 = Trie()  # suffix

        # enumerate() because we need to return index, not a word
        for weight, word in enumerate(words):
            cur = self.trie1

            self.addw(cur, weight)

            for letter in word:
                cur = cur[letter]
                self.addw(cur, weight)

            cur = self.trie2

            self.addw(cur, weight)

            for letter in word[::-1]:
                cur = cur[letter]
                self.addw(cur, weight)

    # Each node in trie has a set containing indices in words
    # but the indices are only for words which pass or end at the current node
    def addw(self, node, w):
        """w is index in words"""
        if WEIGHT not in node:
            node[WEIGHT] = {w}
        else:
            node[WEIGHT].add(w)

    def f(self, prefix: str, suffix: str) -> int:
        cur1 = self.trie1
        for letter in prefix:
            if letter not in cur1:
                return -1
            cur1 = cur1[letter]

        cur2 = self.trie2
        for letter in suffix[::-1]:
            if letter not in cur2:
                return -1
            cur2 = cur2[letter]

        # print(f'cur1[WEIGHT]: {cur1[WEIGHT]}, cur2[WEIGHT]: {cur2[WEIGHT]}')

        # Get intersection and max
        return max(cur1[WEIGHT] & cur2[WEIGHT])


if __name__ == '__main__':
    words = ['apple']
    words = ['apple', 'ae']
    prefix = 'a'
    suffix = 'e'
    # words = ['apple', 'orange']
    # words = ['a', 'ab', 'aa']
    obj = WordFilter(words)
    pprint.pprint(obj.trie)
    print(obj.f(prefix, suffix))
    # print(obj.trie1.keys())
    # print(obj.trie1[False])
    # print(obj.trie1['a'].keys())
    # print(obj.trie1['a'][False])
    # print(obj.trie1['a']['a'].keys())
    # print(obj.trie1['a']['a'][False])


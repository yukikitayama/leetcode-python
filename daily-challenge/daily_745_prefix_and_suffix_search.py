import collections


WORDS = ['apple']
PREFIX = 'a'
SUFFIX = 'e'
WEIGHT = False


Trie = lambda: collections.defaultdict(Trie)


class WordFinder:
    def __init__(self, words):
        self.trie1 = Trie()  # Prefix
        self.trie2 = Trie()  # Suffix

        for weight, word in enumerate(words):

            # Prefix operation
            cur = self.trie1
            self.add_weight(cur, weight)
            print(f'After initial add_weight(cur: {cur}, weight: {weight})')

            for letter in word:
                cur = cur[letter]
                self.add_weight(cur, weight)
                print(f'After add_weight(cur: {cur}, weight: {weight}) with letter: {letter} in word: {word}')

            # Suffix operation
            cur = self.trie2
            self.add_weight(cur, weight)
            print(f'After initial add_weight(cur: {cur}, weight: {weight})')

            for letter in word[::-1]:
                cur = cur[letter]
                self.add_weight(cur, weight)
                print(f'After add_weight(cur: {cur}, weight: {weight}) with letter: {letter} in word: {word}')

    def add_weight(self, node, weight):
        # If False is not in Trie node
        if WEIGHT not in node:
            node[WEIGHT] = {weight}
        else:
            node[WEIGHT].add(weight)


class WordFilter:
    def __init__(self, words):
        self.trie = Trie()

        for weight, word in enumerate(words):
            word += '#'
            for i in range(len(word)):
                cur = self.trie
                cur[WEIGHT] = weight
                for j in range(i, 2 * len(word) - 1):
                    cur = cur[word[j % len(word)]]
                    cur[WEIGHT] = weight

    def f(self, prefix, suffix):
        cur = self.trie
        for letter in suffix + '#' + prefix:
            if letter not in cur:
                return -1
            cur = cur[letter]
        return cur[WEIGHT]


def main():

    obj = WordFilter(words=WORDS)
    param_1 = obj.f(prefix=PREFIX, suffix=SUFFIX)
    print(f'param_1: {param_1}')


if __name__ == '__main__':
    main()

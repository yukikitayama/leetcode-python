"""
b   a   l   l
a   r   e   a
l   e   a   d
l   a   d   y

- step: 1, word_squares: [ball].
  - step: 2, startswith: a, word_squares: [ball, area]
    - step: 3, startswith: le

- Increment pointer index in each backtracking iteration
"""


from typing import List


class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        self.words = words
        self.N = len(words[0])
        self.buildPrefixHashTable(self.words)
        results = []
        for word in words:
            word_squares = [word]
            self.backtracking(1, word_squares, results)
        return results

    def backtracking(self, step, word_squares, results):
        if step == self.N:
            results.append(word_squares[:])
            return

        prefix = ''.join([word[step] for word in word_squares])

        print(f'step: {step}, prefix: {prefix}, word_squares: {word_squares}')

        for candidate in self.getWordsWithPrefix(prefix):
            word_squares.append(candidate)
            self.backtracking(step + 1, word_squares, results)
            word_squares.pop()

    def getWordsWithPrefix(self, prefix):
        # for word in self.words:
        #     if word.startswith(prefix):
        #         yield word

        if prefix in self.prefixHashTable:
            return self.prefixHashTable[prefix]
        else:
            return set()

    def buildPrefixHashTable(self, words):
        # Hashmap with key prefix and value a set of words
        self.prefixHashTable = {}
        for word in words:
            # range starts with 1 because slice end is exclusive
            for prefix in (word[:i] for i in range(1, len(word))):
                # setdefault gets value if the key exists. Otherwise, set the default value
                self.prefixHashTable.setdefault(prefix, set()).add(word)


words = ["area","lead","wall","lady","ball"]
print(Solution().wordSquares(words))


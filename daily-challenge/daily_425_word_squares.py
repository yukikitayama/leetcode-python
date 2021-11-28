from typing import List


class Solution:
    def __init__(self):
        self.words = None
        self.N = None
        self.prefix_to_list_of_words = {}

    def wordSquares(self, words: List[str]) -> List[List[str]]:
        self.words = words
        self.N = len(words[0])
        # Dictionary key: prefix string, value: list of words started with the prefix
        self.build_prefix_hashtable(words)
        # print(self.prefix_to_list_of_words)

        results = []
        for word in words:
            word_squares = [word]
            self.backtracking(1, word_squares, results)
        return results

    def backtracking(self,
                     step: int,
                     word_squares: List[str],
                     results: List[List[str]]) -> None:
        if step == self.N:
            # [:] returns a new object copy of the list
            results.append(word_squares[:])
            return

        # Make a word by extracting a character from each word
        prefix = ''.join([word[step] for word in word_squares])

        for candidate in self.get_words_with_prefix(prefix):
            word_squares.append(candidate)
            self.backtracking(step + 1, word_squares, results)
            # Backtrack
            word_squares.pop()

    def get_words_with_prefix(self, prefix: str) -> List[str]:
        # Can do this because the same word can be used multiple times
        # for word in self.words:
        #     if word.startswith(prefix):
                # yield because we wanna come back here
                # yield word
        if prefix in self.prefix_to_list_of_words:
            return self.prefix_to_list_of_words[prefix]
        else:
            return set([])

    def build_prefix_hashtable(self, words: List[str]) -> None:
        for word in words:
            for prefix in (word[:i] for i in range(1, len(word))):
                self.prefix_to_list_of_words.setdefault(prefix, set()).add(word)


words = ["area","lead","wall","lady","ball"]
print(Solution().wordSquares(words))

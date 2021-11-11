from typing import List
import collections


class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:

        def make_prefix_to_words(words):
            prefix_to_words = collections.defaultdict(set)
            for word in words:
                for prefix in (word[:i] for i in range(1, len(word))):
                    prefix_to_words[prefix].add(word)
            return prefix_to_words

        def backtracking(index, word_squares):

            if index == len(words[0]):
                ans.append(word_squares[:])
                return

            prefix = ''.join([word[index] for word in word_squares])

            for candidate in get_words_with_prefix(prefix):
                word_squares.append(candidate)
                backtracking(index + 1, word_squares)
                word_squares.pop()

        def get_words_with_prefix(prefix):
            if prefix in prefix_to_words:
                return prefix_to_words[prefix]
            else:
                return set()

        prefix_to_words = make_prefix_to_words(words)

        ans = []
        for word in words:
            word_squares = [word]
            backtracking(1, word_squares)

        return ans

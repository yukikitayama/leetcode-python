"""
- Each time make a new subsequence from s
  - Check whether it exists in words
"""


from typing import List


class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:

        def is_subseq(word):
            iterator = iter(s)
            # iterator = s
            return all([char in iterator for char in word])

        return sum(is_subseq(word) for word in words)

s = "abcde"
words = ["a","bb","acd","ace"]
print(Solution().numMatchingSubseq(s, words))

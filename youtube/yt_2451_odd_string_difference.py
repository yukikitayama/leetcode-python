"""
T: O(MN)
S: O(M)
M: length of words array
"""

from typing import List
import collections


class Solution:
    def oddString(self, words: List[str]) -> str:

        def word_to_diff_array(word):
            ans = []

            for i in range(1, len(word)):
                ans.append(ord(word[i]) - ord(word[i - 1]))

            return ans

        diff_array_to_words = collections.defaultdict(list)

        for i in range(len(words)):
            diff_array = word_to_diff_array(words[i])
            diff_array_to_words[tuple(diff_array)].append(words[i])

        for k, v in diff_array_to_words.items():
            if len(v) == 1:
                return v[0]

"""
preprocess
prefix sum
"""

from typing import List


class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:

        targets = []
        for word in words:
            if word[0] in "aeiou" and word[-1] in "aeiou":
                targets.append(1)
            else:
                targets.append(0)

        # print(targets)

        prefix = [0]
        for target in targets:
            prefix.append(prefix[-1] + target)

        # print(prefix)

        ans = []
        for l, r in queries:
            c = prefix[r + 1] - prefix[l]
            ans.append(c)

        return ans
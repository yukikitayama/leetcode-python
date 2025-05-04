"""
if concatenate top and bottom numbers in a domino
  min: 11, max: 99
"""

from typing import List
import collections


class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        counter = [0] * 100
        ans = 0
        for upper, bottom in dominoes:
            key = upper * 10 + bottom if upper < bottom else bottom * 10 + upper
            ans += counter[key]
            counter[key] += 1
        return ans

    def numEquivDominoPairs1(self, dominoes: List[List[int]]) -> int:
        counter = collections.Counter()
        ans = 0
        for d in dominoes:
            k = tuple(sorted(d))
            if k in counter:
                ans += counter[k]
            counter[k] += 1

        return ans
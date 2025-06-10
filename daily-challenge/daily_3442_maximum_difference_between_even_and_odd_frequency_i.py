"""
max odd freq
min even freq
"""

import collections


class Solution:
    def maxDifference(self, s: str) -> int:
        max_odd = 0
        min_even = float("inf")
        counter = collections.Counter(s)
        for k, v in counter.items():
            if v % 2 != 0:
                max_odd = max(max_odd, v)
            elif v % 2 == 0:
                min_even = min(min_even, v)

        return max_odd - min_even

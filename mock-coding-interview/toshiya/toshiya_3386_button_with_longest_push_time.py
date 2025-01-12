"""
T: O(N)
S: O(1)
"""

from typing import List


class Solution:
    def buttonWithLongestTime(self, events: List[List[int]]) -> int:
        ans = float("inf")
        prev_t = 0
        max_so_far = 0

        for i, t in events:

            d = t - prev_t
            if d == max_so_far:
                max_so_far = d
                ans = min(ans, i)
            elif d > max_so_far:
                max_so_far = d
                ans = i
            prev_t = t

        return ans
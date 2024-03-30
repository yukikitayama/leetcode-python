"""
[1, 0, 1, 0]
[1, -1, 1, -1]
total: 0
i: 0, left: 1, right: total - left = 0 - 1 = -1
i: 1, left: 0, right: 0 - 0
i: 2, left: 1, right: 0 - 1 = -1
ans is i + 1 such that this index is minimum and left > right
"""

from typing import List


class Solution:
    def minimumLevels(self, possible: List[int]) -> int:
        pl = [1 if p == 1 else -1 for p in possible]
        total = sum(pl)

        # print(f"total: {total}, pl: {pl}")

        ans = float("inf")
        left = 0
        for i in range(len(pl) - 1):
            left += pl[i]
            right = total - left

            if left > right:
                ans = min(ans, i + 1)

        return -1 if ans == float("inf") else ans

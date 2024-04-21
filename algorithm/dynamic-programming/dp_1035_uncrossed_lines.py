"""
When array lengths are different
  shorter array will be padded with 0
dp[i] represents max number of lines up to i
"""

from typing import List
import functools


class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:

        dp_curr = [0] * (len(nums2) + 1)
        dp_prev = [0] * (len(nums2) + 1)

        for r in range(1, len(nums1) + 1):
            for c in range(1, len(nums2) + 1):

                if nums1[r - 1] == nums2[c - 1]:
                    dp_curr[c] = 1 + dp_prev[c - 1]

                else:
                    dp_curr[c] = max(
                        dp_curr[c - 1],
                        dp_prev[c]
                    )

            dp_prev = dp_curr[:]

        return dp_curr[-1]

    def maxUncrossedLines2(self, nums1: List[int], nums2: List[int]) -> int:

        dp = [[0] * (len(nums2) + 1) for _ in range(len(nums1) + 1)]

        for r in range(1, len(nums1) + 1):
            for c in range(1, len(nums2) + 1):

                if nums1[r - 1] == nums2[c - 1]:
                    dp[r][c] = 1 + dp[r - 1][c - 1]

                else:
                    dp[r][c] = max(
                        dp[r - 1][c],
                        dp[r][c - 1]
                    )

        return dp[-1][-1]

    def maxUncrossedLines1(self, nums1: List[int], nums2: List[int]) -> int:

        @functools.cache
        def dp(p1, p2):

            # Base
            if p1 < 0 or p2 < 0:
                return 0

            if nums1[p1] == nums2[p2]:
                return 1 + dp(p1 - 1, p2 - 1)
            else:
                return max(
                    dp(p1 - 1, p2),
                    dp(p1, p2 - 1)
                )

        return dp(len(nums1) - 1, len(nums2) - 1)
from typing import List
import functools


class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        """Bottom-up DP, S: O(N)"""
        # Edge case: one is all positive and another is all negative
        # If nums1 all are negative and nums2 all are positive
        if max(nums1) < 0 and min(nums2) > 0:
            return max(nums1) * min(nums2)

        # If nums1 all are positive and nums2 all are negative
        elif min(nums1) > 0 and max(nums2) < 0:
            return min(nums1) * max(nums2)

        prev_dp = [0] * (len(nums2) + 1)
        curr_dp = [0] * (len(nums2) + 1)

        for r in range(len(nums1)):
            curr_dp = [0] * (len(nums2) + 1)
            for c in range(len(nums2)):
                curr_dp[c + 1] = max(
                    nums1[r] * nums2[c] + prev_dp[c],
                    prev_dp[c + 1],
                    curr_dp[c]
                )

            prev_dp = curr_dp

        return curr_dp[-1]

    def maxDotProduct2(self, nums1: List[int], nums2: List[int]) -> int:
        """Bottom-up DP, S: O(NM)"""
        # Edge case: one is all positive and another is all negative
        # If nums1 all are negative and nums2 all are positive
        if max(nums1) < 0 and min(nums2) > 0:
            return max(nums1) * min(nums2)

        # If nums1 all are positive and nums2 all are negative
        elif min(nums1) > 0 and max(nums2) < 0:
            return min(nums1) * max(nums2)

        dp = [[0] * (len(nums2) + 1) for _ in range(len(nums1) + 1)]

        for r in range(len(nums1)):
            for c in range(len(nums2)):
                dp[r + 1][c + 1] = max(
                    nums1[r] * nums2[c] + dp[r][c],
                    dp[r + 1][c],
                    dp[r][c + 1]
                )

        # for row in dp:
        #     print(row)

        return dp[-1][-1]

    def maxDotProduct1(self, nums1: List[int], nums2: List[int]) -> int:
        """Top-down DP"""

        # Edge case: one is all positive and another is all negative
        # If nums1 all are negative and nums2 all are positive
        if max(nums1) < 0 and min(nums2) > 0:
            return max(nums1) * min(nums2)

        # If nums1 all are positive and nums2 all are negative
        elif min(nums1) > 0 and max(nums2) < 0:
            return min(nums1) * max(nums2)

        @functools.cache
        def dp(i, j):

            # Base case: exhaust either array
            if i == len(nums1) or j == len(nums2):
                return 0

            return max(
                # Product of current numbers
                nums1[i] * nums2[j] + dp(i + 1, j + 1),
                # Product of current nums1 number and next nums2
                dp(i, j + 1),
                # Product of current nums2 numbwe and next nums1
                dp(i + 1, j)
            )

        return dp(0, 0)
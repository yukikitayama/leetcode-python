"""
sort
two pointers

[0, 1, 5, 10, 14]
"""

from typing import List


class Solution:
    def minDifference(self, nums: List[int]) -> int:

        # Edge case
        if len(nums) <= 4:
            return 0

        nums.sort()
        left = 3
        right = len(nums) - 1
        ans = float("inf")

        for _ in range(4):
            ans = min(
                ans,
                nums[right] - nums[left]
            )
            right -= 1
            left -= 1

        return ans

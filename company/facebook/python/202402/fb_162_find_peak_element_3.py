"""
Binary search
  until search space is 1
"""

from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:

            mid = (left + right) // 2

            if nums[mid] < nums[mid + 1]:
                # Exclude mid
                left = mid + 1
            else:
                # At least mid is higher than right
                # Mid could be peak
                right = mid

        return left

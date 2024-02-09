"""
This is not askingg the peak with maximum
[1, 2, 3, 2, 3, 4, 5, 4]
We can return index of the first 3

Binary search
  Requires array is sorted
  Consider given array as alternating sorted array (alternating ascending and descending)
  Keep searching until only one element remains in the search space
"""

from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:

            mid = (left + right) // 2

            # Go left
            if nums[mid] > nums[mid + 1]:
                # No +1 to mid because nums[mid] could be peak
                right = mid

            # Go right
            else:
                # +1 because nums[mid] is smaller than nums[mid + 1]
                # nums[mid] won't be peak
                left = mid + 1

        return left


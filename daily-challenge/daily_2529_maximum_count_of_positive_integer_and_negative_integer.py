"""
linear scan
  T: O(N)
  S: O(1)

Binary search to find leftmost 0 and rightmost 0
  number of negative is leftmost index
  number of positive is (array length - rightmost index - 1)

The lowerBound() function will return the first index in the array where the value is greater than or equal to zero,
and the upperBound() function will return the first index where the value is strictly greater than zero.
"""

from typing import List
import bisect


class Solution:
    def maximumCount(self, nums: List[int]) -> int:

        def lower_bound():
            left = 0
            right = len(nums) - 1
            res = len(nums)
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < 0:
                    left = mid + 1
                else:
                    res = mid
                    right = mid - 1
            return res

        def upper_bound():
            left = 0
            right = len(nums) - 1
            res = len(nums)
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] <= 0:
                    left = mid + 1
                else:
                    res = mid
                    right = mid - 1
            return res

        num_neg = lower_bound()
        num_pos = len(nums) - upper_bound()
        return max(num_neg, num_pos)

    def maximumCount2(self, nums: List[int]) -> int:

        left = bisect.bisect_left(nums, 0)
        right = bisect.bisect_right(nums, 0)

        num_neg = left
        num_pos = len(nums) - right

        return max(num_neg, num_pos)

    def maximumCount1(self, nums: List[int]) -> int:
        num_pos = 0
        num_neg = 0

        for num in nums:

            if num < 0:
                num_neg += 1
            elif num > 0:
                num_pos += 1

        return max(num_pos, num_neg)

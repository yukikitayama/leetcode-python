"""
Binary search
  if mid num is bigger than left and right
    answer
  if mid num is smaller than right,
    go to right
  if mid num is smaller than left
    go to left

eg
  [1, 2]

Ans
  Reduce search space until the space length is 1
"""

from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        left = 0
        right = len(nums) - 1

        while left < right:
            # If even length, get left one in the center
            mid = (left + right) // 2

            # print(f"left: {left}, mid: {mid}, right: {right}")

            if nums[mid] < nums[mid + 1]:
                # +1 because current mid isn't a candidate for peak because mid + 1 is bigger
                left = mid + 1

            else:
                # No -1 because at least current mid is bigger than the num at the current right
                # so current mid number is still a candidate for peak, so we include it in the range
                right = mid

        # When while loop breaks, left == right, meaning only single element left, which is peak
        return left

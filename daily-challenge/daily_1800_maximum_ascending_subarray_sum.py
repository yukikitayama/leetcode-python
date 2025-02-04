"""
if current is bigger than or equal to prev
  increment current streak
else
  start new streak with curr num
check ans
"""

from typing import List


class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        ans = nums[0]
        streak = nums[0]

        for i in range(1, len(nums)):

            if nums[i] > nums[i - 1]:
                streak += nums[i]

            else:
                streak = nums[i]

            ans = max(ans, streak)

        return ans
"""
streak_inc
max_so_far_inc
streak_dec
max_so_far_dec
max of either max so far
if current is bigger than prev
  count up streak_inc
  streak_dec = 1
if current is smaller than prev
  streak_inc = 1
  count up streak_in

"""

from typing import List


class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        streak_inc = 1
        max_so_far_inc = streak_inc
        streak_dec = 1
        max_so_far_dec = streak_dec
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                streak_inc += 1
                streak_dec = 1
            elif nums[i] < nums[i - 1]:
                streak_inc = 1
                streak_dec += 1
            elif nums[i] == nums[i - 1]:
                streak_inc = 1
                streak_dec = 1
            max_so_far_inc = max(streak_inc, max_so_far_inc)
            max_so_far_dec = max(streak_dec, max_so_far_dec)

        return max(
            max_so_far_inc,
            max_so_far_dec
        )
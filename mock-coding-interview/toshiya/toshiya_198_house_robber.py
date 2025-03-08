"""
scan left to right
  2 choices
    rob this
      money = this + cumulative robbed amount from 2 steps before
    skip this
      money = cumulative robbed amount frm 1 step before

  1 step before becomes 2 steps before cumulative amount
  current money becomes 1 steps before cumulative amount
After scan
  max of 2 cumulative 2 steps before or 1 step before
2 variables
  2 step before cumulative amount
  1 step before cumulative

DP
"""

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        one_step_before = 0
        two_step_before = 0
        for i in range(len(nums)):
            # Rob
            rob = nums[i] + two_step_before
            # Skip
            skip = one_step_before

            # Get best scenario at current step
            curr_best_scenario = max(rob, skip)

            # To iterate next
            two_step_before = one_step_before
            one_step_before = curr_best_scenario

        return curr_best_scenario

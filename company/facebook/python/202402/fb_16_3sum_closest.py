"""
Sort
three pointer
  leftmost base
  left
  right

[-4, -1, 1, 2]
  [-4, -1, 2], sum: -3, cannot increase any more, no further iteration
  [-1, 1, 2], sum: 2
"""

from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()

        abs_min_diff_so_far = float("inf")

        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1

            while left < right:

                sum_ = nums[i] + nums[left] + nums[right]

                if abs(target - sum_) < abs_min_diff_so_far:
                    ans = sum_
                    abs_min_diff_so_far = abs(target - sum_)

                if sum_ < target:
                    left += 1
                elif sum_ > target:
                    right -= 1
                elif sum_ == target:
                    return sum_

        return ans

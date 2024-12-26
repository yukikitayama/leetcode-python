from typing import List
import functools


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        @functools.cache
        def dp(index, sum_):

            if index == len(nums):
                if sum_ == target:
                    return 1
                else:
                    return 0

            # Add
            add = dp(index + 1, sum_ + nums[index])

            # Subtract
            subtract = dp(index + 1, sum_ - nums[index])

            return add + subtract

        return dp(0, 0)
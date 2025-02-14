from typing import List
import functools


class Solution:
    def jump(self, nums: List[int]) -> int:

        @functools.cache
        def dp(index):

            if index >= len(nums) - 1:
                return 0

            res = float("inf")
            for step in range(nums[index], 0, -1):
                res = min(
                    res,
                    dp(index + step) + 1
                )

            return res

        return dp(0)
from typing import List
import functools


class Solution:
    def maxCoins(self, nums: List[int]) -> int:

        # Special case
        # All the integers in nums are the same
        if len(nums) > 1 and len(set(nums)) == 1:
            return (nums[0] ** 3) * (len(nums) - 2) + nums[0] ** 2 + nums[0]

        # Edge case
        nums = [1] + nums + [1]

        @functools.lru_cache(None)
        def dp(left, right):
            if right - left < 0:
                return 0

            result = 0

            for i in range(left, right + 1):
                gain = nums[left - 1] * nums[i] * nums[right + 1]
                remaining = dp(left, i - 1) + dp(i + 1, right)
                result = max(result, remaining + gain)
            return result

        # 1 because 0 is the appended [1], which it doesn't have to burst
        # -2 because 0 at the end and additional -1 to avoid index out of bound
        return dp(1, len(nums) - 2)



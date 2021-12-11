"""
- top-down dp
- dp(i) = max(dp(i - 1), nums[i] + dp(i - 2))
- dp(0): nums[0]
- dp(1): max(nums[0], nums[1])
"""


from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:

        def dp(i):
            if i == 0:
                return nums[0]
            if i == 1:
                return max(nums[0], nums[1])
            if i not in memo:
                memo[i] = max(dp(i - 1), nums[i] + dp(i - 2))
            return memo[i]

        memo = {}

        return dp(len(nums) - 1)



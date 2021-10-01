"""
- dp[i] represents the number of combinations that sum up to the value of i
"""


from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0 for i in range(target + 1)]
        dp[0] = 1

        for comb_sum in range(target + 1):
            for num in nums:
                if comb_sum - num >= 0:
                    dp[comb_sum] += dp[comb_sum - num]

        return dp[target]


nums = [1, 2, 3]
target = 4
print(Solution().combinationSum4(nums, target))


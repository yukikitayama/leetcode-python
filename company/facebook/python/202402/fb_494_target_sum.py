"""
Backtracking
  recursion with index to nums, curr sum
  at each index, we have 2 choices, * 1 or * -1

sum: 5, target: 3, we need -2

Multiple times same index and same current sum
memo[i][current sum + sum of given nums]
  Addition of given nums sum makes the index positive
    eg. [-1, -1, -1], current sum: -3, nums sum: 3, -3 + 3 = 0
"""

from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        total = sum(nums)

        # Edge case
        if target > total:
            return 0

        # dp[i][sum]: count
        dp = [[0] * (2 * total + 1) for _ in range(len(nums))]

        # Base
        dp[0][nums[0] + total] = 1
        # += 1 because if nums[0] is 0, we have two ways as base case -1 * 0 and 1 * 0 even if the values are the same
        dp[0][-nums[0] + total] += 1

        for i in range(1, len(nums)):
            for sum_ in range(-total, total + 1):
                # sum_ + total is shifting to get positive integer index
                if dp[i - 1][sum_ + total] > 0:
                    # New count is based on previous count
                    dp[i][nums[i] + sum_ + total] += dp[i - 1][sum_ + total]
                    dp[i][-nums[i] + sum_ + total] += dp[i - 1][sum_ + total]

        # for row in dp:
        #     print(row)

        return dp[-1][target + total]

    def findTargetSumWays1(self, nums: List[int], target: int) -> int:

        ans = 0

        def backtracking(index, curr_sum):
            nonlocal ans

            # Terminate recursion
            if index == len(nums):
                if curr_sum == target:
                    ans += 1
                return

            for c in [1, -1]:
                backtracking(index + 1, curr_sum + c * nums[index])

        backtracking(0, 0)

        return ans

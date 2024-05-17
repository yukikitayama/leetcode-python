"""
dp(remaining)
  Base case
    if remaining is 0, return 1 as one combination is made
    if remaining is negative, return 0
  current answer 0
  for each number
    increment current answer by dp(remaining - current number)

dp(target)

Follow up
  if numbers contain negative number
"""

from typing import List
import functools


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:

        dp = [0] * (target + 1)

        # Base case
        dp[0] = 1

        for i in range(1, target + 1):

            for num in nums:

                if i - num >= 0:
                    dp[i] += dp[i - num]

        # print(dp)

        return dp[target]

    def combinationSum41(self, nums: List[int], target: int) -> int:

        @functools.cache
        def dp(remaining):

            # Base case:
            if remaining == 0:
                return 1
            elif remaining < 0:
                return 0

            ans = 0
            for num in nums:
                ans += dp(remaining - num)
            return ans

        return dp(target)

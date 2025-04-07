"""
dp
  base case
    index is at the end of nums
    return true if curr sum if half of the total sum
For each element
  include
  exclude
"""

from typing import List
import functools


class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        total_sum = sum(nums)
        if total_sum % 2 != 0:
            return False
        subset_sum = total_sum // 2
        n = len(nums)

        dp = [[False] * (subset_sum + 1) for _ in range(n + 1)]
        # 0 subset sum can be achieved by not including any numbers
        dp[0][0] = True

        for curr_index in range(1, n + 1):
            curr_num = nums[curr_index - 1]

            for curr_sum in range(subset_sum + 1):

                # If curr sum is smaller than a number, we cannot include the number, because of negative sum
                if curr_sum < curr_num:
                    dp[curr_index][curr_sum] = dp[curr_index - 1][curr_sum]

                else:
                    # Exclude or include
                    dp[curr_index][curr_sum] = dp[curr_index - 1][curr_sum] or dp[curr_index - 1][curr_sum - curr_num]

        return dp[n][subset_sum]

    def canPartition1(self, nums: List[int]) -> bool:

        total = sum(nums)

        # Edge case
        if total % 2 != 0:
            return False

        subset_sum = total // 2

        @functools.cache
        def dp(index, curr_sum):
            if curr_sum == 0:
                return True
            if index == len(nums) or curr_sum < 0:
                return False

            res = dp(index + 1, curr_sum - nums[index]) or dp(index + 1, curr_sum)

            return res

        return dp(0, subset_sum)

"""
dp[i]
  minimum number of jumps to nums[i]

  dp[0]: 0
  dp[1]: if j + nums[j] >= i, dp[i] + 1

  T: O(N**2)
"""

from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        ans = 0

        curr_end = 0
        next_end = 0

        # -1 because when we reach the last element, incrementation occurs again
        # The problem says we are guaranteed to reach the last,
        # so we don't need to test the last element
        for i in range(len(nums) - 1):

            next_end = max(next_end, i + nums[i])

            if i == curr_end:
                ans += 1
                curr_end = next_end

        return ans

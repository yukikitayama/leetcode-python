from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:

        curr_jump_end = 0
        farthest = 0
        ans = 0
        # up to n - 2 index, because guarantee to reach
        for i in range(len(nums) - 1):

            farthest = max(farthest, i + nums[i])

            if i == curr_jump_end:
                ans += 1
                curr_jump_end = farthest

        return ans

    def jump1(self, nums: List[int]) -> int:
        dp = [float("inf")] * len(nums)
        # Base
        dp[-1] = 0
        for i in range(len(nums) - 1, -1, -1):
            furthest = min(i + nums[i], len(nums) - 1)
            for j in range(i + 1, furthest + 1):
                dp[i] = min(dp[i], dp[j] + 1)

        return dp[0]
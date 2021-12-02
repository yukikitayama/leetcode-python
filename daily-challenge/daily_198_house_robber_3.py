"""
- bottom up dp
"""


from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not len(nums):
            return 0

        # +1 for 0 house case
        dp = [0] * (len(nums) + 1)

        # Base case
        # It won't be index out of bound error
        # because, checking length 0 at the top,
        # and dp is one length longer than nums
        dp[len(nums)] = 0
        dp[len(nums) - 1] = nums[-1]

        for i in range(len(nums) - 2, -1, -1):
            dp[i] = max(nums[i] + dp[i + 2], dp[i + 1])

        return dp[0]


nums = [1,2,3,1]  # 4
nums = [2,7,9,3,1]  # 12
print(Solution().rob(nums))


from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Base case is length one character
        dp = [1] * len(nums)

        for i in range(1, len(nums)):

            for j in range(i):

                if nums[i] > nums[j]:

                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)


"""
dp[i] represents the longest increasing subsequence ending at index i
"""


nums = [10,9,2,5,3,7,101,18]
print(Solution().lengthOfLIS(nums))


"""
Algorithm, Bottom up dp
- dp[i] represents the length of the longest increasing subsequence that ends with the ith element
- dp[i] = max(dp[j]) + 1 for all j where j < i and nums[j] < nums[i]
- Base case dp[all indices] are 1 because one character is a subset of increasing subsequence.
- Return max(dp)

Complexity
- Time is O(n^2) for the nested for loops
- Space is O(n) for DP array
"""


from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)

        for right in range(len(nums)):
            for left in range(right):

                if nums[right] > nums[left]:

                    dp[right] = max(dp[right], dp[left] + 1)

        # print(f'dp: {dp}')

        return max(dp)


nums = [10,9,2,5,3,7,101,18]
nums = [5, 6, 7, 8, 1, 2, 3]
print(Solution().lengthOfLIS(nums))

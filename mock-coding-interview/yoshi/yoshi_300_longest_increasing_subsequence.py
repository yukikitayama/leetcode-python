"""
Brute force
  T: O(N**2)

Stack
"""

from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)

        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)

    def lengthOfLIS1(self, nums: List[int]) -> int:
        ans = 0

        def backtracking(comb, index):
            nonlocal ans

            if index == len(nums):
                ans = max(ans, len(comb))
                return

            for i in range(index, len(nums)):

                if not comb:
                    comb.append(nums[i])
                    backtracking(comb, i + 1)
                    comb.pop()
                else:
                    if nums[i] > comb[-1]:
                        comb.append(nums[i])
                        backtracking(comb, i + 1)
                        comb.pop()

                    else:
                        backtracking(comb, i + 1)

        backtracking([], 0)

        return ans

"""
Monotonic stack
  append if current is bigger than stack top
  pop if current is smaller than stack top

Ans
  dp
"""

from typing import List
import bisect


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        sub = [nums[0]]

        for i in range(1, len(nums)):

            if nums[i] > sub[-1]:
                sub.append(nums[i])

            # Binary search
            else:
                j = bisect.bisect_left(sub, nums[i])
                sub[j] = nums[i]

        return len(sub)

    def lengthOfLIS2(self, nums: List[int]) -> int:

        sub = [nums[0]]

        for i in range(1, len(nums)):

            if nums[i] > sub[-1]:
                sub.append(nums[i])
                # print(" ", sub)

            else:
                # Replace subsequence num that is next greater to current number
                # This creates T: O(N**2)
                j = 0
                while nums[i] > sub[j]:
                    j += 1
                sub[j] = nums[i]

                # print(sub)

        # print(sub)

        return len(sub)

    def lengthOfLIS1(self, nums: List[int]) -> int:

        dp = [1] * len(nums)

        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[j] + 1, dp[i])

        return max(dp)

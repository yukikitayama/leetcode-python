"""
Hashmap
  k: num
  v: max length ending at this num

Ans
  dp[right][diff]
    represents length of longest arithmetic sequence ending at right and has diff difference
    if left < right and diff = nums[right] - nums[left]
      dp[right][diff] = dp[left][diff] + 1
"""

from typing import List


class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:

        dp = dict()

        for right in range(len(nums)):
            for left in range(right):

                diff = nums[right] - nums[left]

                if (left, diff) in dp:
                    dp[(right, diff)] = dp[(left, diff)] + 1
                else:
                    # 2 because we start with forming a 2 length sequence by left num and right num
                    dp[(right, diff)] = 2

        # print(dp)

        return max(dp.values())
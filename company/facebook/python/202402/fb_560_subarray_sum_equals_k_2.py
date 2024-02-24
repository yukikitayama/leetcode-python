"""
Two pointers

Ans
  sum[1] is nums[0]
  sum[2] is nums[0] + nums[1]
  sum[3] is nums[0] + nums[1] + nums[2]
  sum(nums[1], nums[2]) is sum[3] - sum[1]
    sum(nums[1:2 inclusive]) = sum[3] - sum[1]
"""

from typing import List
import collections


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # ans = 0

        # prefix_sum = [0]
        # for i in range(len(nums)):
        #     prefix_sum.append(prefix_sum[-1] + nums[i])

        # for start in range(len(nums)):
        #     for end in range(start + 1, len(nums) + 1):
        #         if prefix_sum[end] - prefix_sum[start] == k:
        #             ans += 1

        # return ans

        ans = 0
        sum_ = 0
        sum_to_count = collections.defaultdict(int)
        sum_to_count[sum_] = 1

        for i in range(len(nums)):
            sum_ += nums[i]

            if sum_ - k in sum_to_count:
                ans += sum_to_count[sum_ - k]

            sum_to_count[sum_] += 1

        return ans
"""
[-1, -1, 1]

[-1, -2, 1]
[0, 1, 2, 3]

[1, -1, 0]
[0, 1, 0, 0]
"""

from typing import List
import collections


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum_to_count = collections.Counter()
        prefix_sum = 0
        prefix_sum_to_count[prefix_sum] += 1
        ans = 0

        for i in range(len(nums)):
            prefix_sum += nums[i]

            if prefix_sum - k in prefix_sum_to_count:
                ans += prefix_sum_to_count[prefix_sum - k]

            prefix_sum_to_count[prefix_sum] += 1

        return ans

    def subarraySum1(self, nums: List[int], k: int) -> int:
        ans = 0
        left = 0
        sum_ = 0

        for right in range(len(nums)):
            sum_ += nums[right]

            while sum_ > k and left < right:
                sum_ -= nums[left]
                left += 1

            if sum_ == k:
                ans += 1

        return ans

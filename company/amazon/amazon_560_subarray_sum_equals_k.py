"""
nums: [1, 2, 3, 4]
prefix_sum: [1, 3, 6, 10]
sum of subarray from i to j
prefix_sum[j] - prefix_sum[i - 1]
k = prefix_sum[j] - prefix_sum[i - 1]
prefix_sum[i - 1] = prefix_sum[j] - k
becuase of negative numbers, multiple times to experience the same value of previously seen prefix sum
"""

from typing import List
import collections


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        ans = 0
        prefix_sum_to_count = collections.Counter()
        prefix_sum = 0
        prefix_sum_to_count[prefix_sum] += 1

        for i in range(len(nums)):

            prefix_sum += nums[i]

            if prefix_sum - k in prefix_sum_to_count:
                ans += prefix_sum_to_count[prefix_sum - k]

            prefix_sum_to_count[prefix_sum] += 1

        return ans

    def subarraySum1(self, nums: List[int], k: int) -> int:

        ans = 0
        for left in range(len(nums)):
            sum_ = 0
            for right in range(left, len(nums)):
                sum_ += nums[right]
                if sum_ == k:
                    ans += 1
        return ans


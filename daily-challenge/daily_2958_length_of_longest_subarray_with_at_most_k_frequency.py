"""
Iterate array
  Lazy update max heap
"""

from typing import List
import collections


class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        num_to_count = collections.Counter()
        left = 0
        num_char_over_k = 0

        for right in range(len(nums)):

            num_to_count[nums[right]] += 1

            if num_to_count[nums[right]] == k + 1:
                num_char_over_k += 1

            if num_char_over_k > 0:
                num_to_count[nums[left]] -= 1

                if num_to_count[nums[left]] == k:
                    num_char_over_k -= 1

                left += 1

        # ?
        return len(nums) - left

    def maxSubarrayLength1(self, nums: List[int], k: int) -> int:

        num_to_count = collections.Counter()
        ans = 1
        left = 0

        for right in range(len(nums)):

            num_to_count[nums[right]] += 1

            while num_to_count[nums[right]] > k:
                num_to_count[nums[left]] -= 1
                left += 1

            ans = max(ans, right - left + 1)

        return ans

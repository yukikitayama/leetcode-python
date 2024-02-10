"""
Sliding window
  expand
    if next is 1
    if next is 0 and if we have remaining k
      decrement k
  contract
    if remaining k is 0
    if curr is 0, increment remaining k after contracting

  length is right - left + 1
"""

from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

        ans = 0

        left = 0

        for right in range(len(nums)):

            if nums[right] == 0:
                k -= 1

            if k >= 0:
                ans = max(ans, right - left + 1)

            while left < right and k < 0:
                if nums[left] == 0:
                    k += 1
                left += 1

        return ans
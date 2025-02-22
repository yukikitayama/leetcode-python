"""
sliding window
  hashmap
"""

from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter = 0
        ans = 0
        left = 0
        for right in range(len(nums)):

            if nums[right] == 0:
                counter += 1

            while counter > 1 and left < right:
                if nums[left] == 0:
                    counter -= 1
                left += 1

            ans = max(ans, right - left + 1)

        return ans
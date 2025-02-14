"""
Find start number
  start number is the number which doesn't have previous number
"""

from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        ans = 0
        # Reduce time by avoid restarting from the duplicated numbers
        for num in nums_set:
            if num - 1 not in nums_set:
                streak = 1

                while num + 1 in nums_set:
                    streak += 1
                    num += 1

                ans = max(ans, streak)

        return ans
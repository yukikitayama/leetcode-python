"""
X * 2 > is to check whether being majority
"""

from typing import List
import collections


class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        first_counter = collections.Counter()
        second_counter = collections.Counter(nums)

        for i in range(len(nums)):
            num = nums[i]
            second_counter[num] -= 1
            first_counter[num] += 1

            # Check dominance
            if first_counter[num] * 2 > i + 1 and second_counter[num] * 2 > len(nums) - i - 1:
                return i

        return -1
"""
max_so_far
curr_sum
"""

from typing import List


class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        ans = []

        max_so_far = 0
        curr_sum = 0

        for i in range(len(nums)):

            max_so_far = max(max_so_far, nums[i])
            curr_num = nums[i] + max_so_far
            curr_sum += curr_num

            ans.append(curr_sum)

        return ans
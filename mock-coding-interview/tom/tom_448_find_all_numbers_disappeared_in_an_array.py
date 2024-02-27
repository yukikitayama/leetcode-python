"""
[1, 2, 2, 4]
[-1, -2, 2, -4]
i: 2
"""

from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            abs_num = abs(nums[i])
            if nums[abs_num - 1] > 0:
                nums[abs_num - 1] *= -1

        ans = []
        for i in range(len(nums)):
            if nums[i] > 0:
                ans.append(i + 1)
        return ans

    def findDisappearedNumbers1(self, nums: List[int]) -> List[int]:
        nums_set = set(nums)

        ans = []
        for i in range(1, len(nums) + 1):
            if i not in nums_set:
                ans.append(i)
        return ans
"""
3 arrays
two pointers
"""

from typing import List


class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:

        ans = [pivot] * len(nums)
        left = 0
        right = len(nums) - 1

        for i in range(len(nums)):
            j = len(nums) - 1 - i
            if nums[i] < pivot:
                ans[left] = nums[i]
                left += 1
            if nums[j] > pivot:
                ans[right] = nums[j]
                right -= 1

        return ans

    def pivotArray1(self, nums: List[int], pivot: int) -> List[int]:
        before = []
        middle = []
        after = []
        for num in nums:
            if num < pivot:
                before.append(num)
            elif num == pivot:
                middle.append(num)
            elif num > pivot:
                after.append(num)
        return before + middle + after

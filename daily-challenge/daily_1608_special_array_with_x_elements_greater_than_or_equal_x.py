"""
[0, 0, 3, 4, 4]

if x isn't -1
  x is from 1 to array length
"""

from typing import List


class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()

        def binary_search(target):
            left = 0
            right = len(nums) - 1
            res = -1
            while left <= right:
                mid = (left + right) // 2
                if target <= nums[mid]:
                    res = mid
                    right = mid - 1
                else:
                    left = mid + 1
            return res

        ans = -1
        for x in range(1, len(nums) + 1):
            idx = binary_search(x)
            # [1, 2, 3, 4], idx: 1, num elements: 3 ([2, 3, 4]), ans: len - idx
            count = len(nums) - idx
            if count == x:
                ans = x
        return ans

    def specialArray1(self, nums: List[int]) -> int:
        ans = -1

        for i in range(1, len(nums) + 1):
            count = 0
            for j in range(len(nums)):
                if nums[j] >= i:
                    count += 1
            if count == i:
                ans = i

        return ans
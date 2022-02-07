"""
- two pointers?
"""


from typing import List


# This solution is more efficient when matching with val is rare
# because we copy number only when matched
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        n = len(nums)
        while i < n:
            if nums[i] == val:
                nums[i] = nums[n - 1]
                n -= 1
            else:
                i += 1
        return i


class Solution1:
    def removeElement(self, nums: List[int], val: int) -> int:
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] == val:
                continue
            elif nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
        return slow
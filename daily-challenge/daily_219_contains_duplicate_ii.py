"""
- Two pointers
"""


from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        nums_set = set()

        for i in range(len(nums)):

            if nums[i] in nums_set:
                return True

            nums_set.add(nums[i])

            if len(nums_set) > k:
                nums_set.remove(nums[i - k])

        return False



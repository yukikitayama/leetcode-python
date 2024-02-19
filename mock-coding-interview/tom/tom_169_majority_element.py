from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0

        for i in range(len(nums)):
            if count == 0:
                candidate = nums[i]

            if nums[i] == candidate:
                count += 1
            elif nums[i] != candidate:
                count -= 1

        return candidate
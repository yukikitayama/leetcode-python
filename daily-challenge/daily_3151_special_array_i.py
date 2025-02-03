from typing import List


class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        parity = nums[0] % 2

        for i in range(1, len(nums)):

            if nums[i] % 2 == parity:
                return False

            parity = nums[i] % 2

        return True
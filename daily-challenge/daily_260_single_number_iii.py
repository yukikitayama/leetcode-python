"""
- Linear time
- Constant space
"""


from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        # Get x ^ y
        # x and y are numbers appearing only once
        # x ^ y is alo the difference between the two
        bitmask = 0
        for num in nums:
            bitmask ^= num

        # Get rightmost 1-bit
        diff = bitmask & (~bitmask + 1)
        # diff = bitmask & (-bitmask)

        x = 0
        for num in nums:

            # other once number is screened out because it has no rightmost 1-bit
            # same as another once number
            if num & diff:
                x ^= num

        # y is the 1-bit in bitmask which not appearing in x
        return [x, bitmask ^ x]


nums = [1,2,1,3,2,5]
print(Solution().singleNumber(nums))


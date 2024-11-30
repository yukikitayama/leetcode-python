"""
2: 010
4: 100
OR: 110

8: 1000
4: 0100
Least significant bit
"""


class Solution:
    def hasTrailingZeros(self, nums: List[int]) -> bool:
        evens = 0
        for num in nums:
            if num % 2 == 0:
                evens += 1
        return evens >= 2
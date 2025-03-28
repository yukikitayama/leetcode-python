"""
each distinct number needs to have even number of occurrence
"""

from typing import List
import collections


class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        counter = collections.Counter(nums)
        return all(c % 2 == 0 for c in counter.values())

    def divideArray1(self, nums: List[int]) -> bool:
        counter = collections.Counter(nums)
        for v in counter.values():
            if v % 2 != 0:
                return False
        return True

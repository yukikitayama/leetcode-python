from typing import List
import collections


class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        uniques = []
        counter = collections.Counter(nums)
        for k, v in counter.items():
            if v == 1:
                uniques.append(k)

        if uniques:
            return max(uniques)
        else:
            return -1
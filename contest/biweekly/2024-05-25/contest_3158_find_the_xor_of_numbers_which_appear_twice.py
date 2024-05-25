from typing import List
import collections


class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        counter = collections.Counter(nums)

        if max(counter.values()) == 1:
            return 0

        else:
            ans = 0
            for k, v in counter.items():
                if v == 2:
                    ans ^= k
            return ans
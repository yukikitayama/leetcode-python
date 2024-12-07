from typing import List
import math


class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:

        def is_possible(m):
            c = 0
            for num in nums:
                c += math.ceil(num / m) - 1
                if c > maxOperations:
                    return False
            return True

        l = 1
        r = max(nums)

        while l < r:
            m = (l + r) // 2

            if is_possible(m):
                r = m
            else:
                l = m + 1

        return l
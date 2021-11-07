from typing import List
import random


class Solution:
    def __init__(self, w: List[int]):
        self.prefix_sums = []
        prefix_sum = 0
        for weight in w:
            prefix_sum += weight
            self.prefix_sums.append(prefix_sum)

        self.total_sum = prefix_sum

    def pickIndex(self) -> int:
        left = 0
        right = len(self.prefix_sums) - 1

        target = random.random() * self.total_sum

        # w: [1, 2, 3, 4, 5]
        # prefix: [1, 3, 6, 10, 15]
        # target: 3.5
        # left: 0, right: 4,
        # mid: 0 + 2 = 2,
        # prefix[2]: 6 > target
        # right: 2
        # mid: 0 + 1 = 1,
        # predix[1]: 3 < target
        # left: 2,
        # while: F,
        # return left: 2

        # If while left <= right,
        # mid: 2 + (2 - 2) // 2 = 2
        # self.prefix[2]: 6 > target
        # right: 2, no end of loop
        while left < right:
            mid = left + (right - left) // 2
            if self.prefix_sums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left


"""
Complexity
- Time is O(logn) to pickIndex() by using binary search
"""

w = [1, 3]
print(Solution(w))

"""
w: [1, 3, 7]
prefix_sum: [1, 4, 11]
threshold: 3
Return: 1 (index, not weight)
"""

from typing import List
import bisect
import random


class Solution:

    # Memori limit exceed
    # def __init__(self, w: List[int]):
    #     self.nums = []
    #     for i in range(len(w)):
    #         for _ in range(w[i]):
    #             self.nums.append(i)

    # def pickIndex(self) -> int:
    #     return random.choice(self.nums)

    def __init__(self, w: List[int]):
        self.prefix_sum = [w[0]]
        for i in range(1, len(w)):
            self.prefix_sum.append(self.prefix_sum[-1] + w[i])
        self.total = self.prefix_sum[-1]

    # Accepted but not fast
    # def pickIndex(self) -> int:
    #     threshold = random.random() * self.total
    #     for i in range(len(self.prefix_sum)):
    #         if threshold < self.prefix_sum[i]:
    #             return i

    def pickIndex(self) -> int:
        threshold = random.random() * self.total
        return bisect.bisect_left(self.prefix_sum, threshold)

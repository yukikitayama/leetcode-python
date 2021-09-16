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

        # print(self.prefix_sums)

    def pickIndex(self) -> int:
        target = self.total_sum * random.random()

        # print(f'target: {target}')

        for i, prefix_sum in enumerate(self.prefix_sums):
            if target < prefix_sum:
                return i


"""
Time complexity
Let n be the length of weight
O(n) for constructor, O(n) for pick index

Space complexity
O(n) for constructor, and O(1) for pickIndex
"""


w = [1, 9]
solution = Solution(w)
solution.pickIndex()



from typing import List
import random


class Solution:
    def __init__(self, w: List[int]):
        self.prefix_sums = []
        prefix_sum = 0
        for weight in w:
            prefix_sum += weight
            self.prefix_sums.append(prefix_sum)

        # print(self.prefix_sums)

        self.total_sum = prefix_sum

    def pickIndex(self) -> int:
        target = random.random() * self.total_sum
        for i, prefix_sum in enumerate(self.prefix_sums):
            if target < prefix_sum:
                return i


"""
Complexity
- Time
  - Constructor takes O(n) to make prefix sum array
  - pickIndex() takes O(n) to iterate the n length array
"""

w = [1, 3]
print(Solution(w))

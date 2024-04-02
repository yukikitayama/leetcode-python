from typing import List
import random


class Solution:

    def __init__(self, w: List[int]):
        # Prefix sum array is increasing order, sorted
        self.prefix_sums = []
        prefix_sum = 0
        for i in range(len(w)):
            prefix_sum += w[i]
            self.prefix_sums.append(prefix_sum)

    def pickIndex(self) -> int:
        # Use binary search to find the left insertion location of target
        target = random.random() * self.prefix_sums[-1]

        left = 0
        right = len(self.prefix_sums) - 1

        while left <= right:
            mid = (left + right) // 2

            # Invalid
            if self.prefix_sums[mid] > target:
                right = mid - 1

            # Valid
            elif self.prefix_sums[mid] < target:
                left = mid + 1

        return left


class Solution1:

    def __init__(self, w: List[int]):
        self.prefix_sums = []
        prefix_sum = 0
        for i in range(len(w)):
            prefix_sum += w[i]
            self.prefix_sums.append(prefix_sum)

    def pickIndex(self) -> int:
        target = random.random() * self.prefix_sums[-1]

        for i in range(len(self.prefix_sums)):
            if target < self.prefix_sums[i]:
                return i

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
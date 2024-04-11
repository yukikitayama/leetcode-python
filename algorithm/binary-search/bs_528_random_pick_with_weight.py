"""
Create cumulative probability array
  w: [1, 3]
  cp: [0.25, 1]
pickIndex
  pick random number between 0 and 1
  return left insertion index
"""

from typing import List
import random


class Solution:

    def __init__(self, w: List[int]):
        self.cum_prob = []
        sum_ = sum(w)
        curr_cum_prob = 0
        for i in range(len(w)):
            curr_cum_prob += w[i] / sum_
            self.cum_prob.append(curr_cum_prob)

    def pickIndex(self) -> int:
        r = random.random()

        left = 0
        right = len(self.cum_prob)
        while left <= right:
            mid = (left + right) // 2

            if self.cum_prob[mid] == r:
                return mid
            elif self.cum_prob[mid] > r:
                right = mid - 1
            elif self.cum_prob[mid] < r:
                left = mid + 1
        return left

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
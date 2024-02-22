"""
Random choice with weight
cumulative distribution function
  [1, 3], random number between 0 to 1 but scaly by 4 (sum of weights)
  compute prefix sum of weight
    [0, 1, 4]
      if 0 <= random < 1, pick 1
      if 1 <= random < 4, pick 3
"""

from typing import List
import random


class Solution:

    def __init__(self, w: List[int]):
        # self.prefix_sum = [0]
        # for i in range(len(w)):
        #     self.prefix_sum.append(self.prefix_sum[-1] + w[i])
        # self.sum_ = sum(w)

        self.prefix_sum = []
        prefix_sum = 0
        for i in range(len(w)):
            prefix_sum += w[i]
            self.prefix_sum.append(prefix_sum)
        self.sum_ = prefix_sum

    def pickIndex(self) -> int:
        scaled_random = random.random() * self.sum_
        # for i in range(1, len(self.prefix_sum)):
        #     if self.prefix_sum[i - 1] < scaled_random <= self.prefix_sum[i]:
        #         return i - 1

        # for i in range(len(self.prefix_sum)):
        #     if scaled_random < self.prefix_sum[i]:
        #         return i

        # return bisect.bisect_left(self.prefix_sum, scaled_random)

        # w: [1, 2], prefix_sum: [1, 3], random: 1.2
        # w: [1, 2], prefix_sum: [1, 3], random: 0.2
        left = 0
        right = len(self.prefix_sum) - 1
        while left < right:
            mid = left + (right - left) // 2

            curr_weight = self.prefix_sum[mid]

            if scaled_random < curr_weight:
                right = mid
            else:
                left = mid + 1

        return left

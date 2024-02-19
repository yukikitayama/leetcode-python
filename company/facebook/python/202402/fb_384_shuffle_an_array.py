"""
Naive
  init saves the array
  reset returns the saved original array
  shuffle copies the saved array
    random choice index to the array
    pop the number and append to the answer array
    repeat n times
    T: O(N^2)

Shuffle needs to optimize time
"""

from typing import List
import random


class Solution:

    def __init__(self, nums: List[int]):
        # original is always copy
        self.original = nums[:]
        self.curr = nums

    def reset(self) -> List[int]:
        self.curr = self.original
        self.original = self.original[:]
        return self.curr

    def shuffle(self) -> List[int]:
        # curr = self.curr[:]

        # for fixed_i in range(len(curr)):

        #     # curr length dynamically shrink
        #     i = random.randrange(len(curr))
        #     self.curr[fixed_i] = curr.pop(i)

        # return self.curr

        n = len(self.curr)

        for i in range(n):
            j = random.randrange(i, n)
            self.curr[i], self.curr[j] = self.curr[j], self.curr[i]

        return self.curr

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
from typing import List
import collections
import random


class Solution:

    def __init__(self, nums: List[int]):
        self.num_to_indices = collections.defaultdict(list)
        for i in range(len(nums)):
            self.num_to_indices[nums[i]].append(i)

    def pick(self, target: int) -> int:
        indices = self.num_to_indices[target]
        return random.choice(indices)

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
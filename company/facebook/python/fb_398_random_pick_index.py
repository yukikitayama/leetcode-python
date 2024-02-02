from typing import List
import collections
import random


class Solution:
    def __init__(self, nums: List[int]):
        self.indices = collections.defaultdict(list)
        for i in range(len(nums)):
            self.indices[nums[i]].append(i)

        # print(self.indices)

    def pick(self, target: int) -> int:
        i = random.randint(0, len(self.indices[target]) - 1)
        return self.indices[target][i]


if __name__ == '__main__':
    nums = [1, 2, 3, 3, 3]
    obj = Solution(nums)
    print(obj.pick(3))

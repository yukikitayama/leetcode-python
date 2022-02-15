from typing import List
import collections


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        count = collections.Counter({0: 1})

        for num in nums:

            step = collections.Counter()

            for c in count:
                step[c + num] += count[c]
                step[c - num] += count[c]

            count = step

            print(f'count: {count}')

        return count[target]


if __name__ == '__main__':
    nums = [1, 1, 1, 1, 1]
    target = 3
    # 5
    print(Solution().findTargetSumWays(nums, target))

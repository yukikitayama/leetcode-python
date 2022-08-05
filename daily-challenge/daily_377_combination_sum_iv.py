"""
- backtracking, dp
"""


from typing import List
import functools


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:

        @functools.lru_cache(maxsize=None)
        def recursion(remain):

            if remain == 0:
                return 1

            ans = 0

            for num in nums:
                if remain - num >= 0:
                    ans += recursion(remain - num)

            return ans

        return recursion(target)


if __name__ == '__main__':
    nums = [1, 2, 3]
    target = 4
    print(Solution().combinationSum4(nums, target))

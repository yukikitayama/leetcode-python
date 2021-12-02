"""
- lru_cache
"""


from typing import List
import functools


class Solution:
    def rob(self, nums: List[int]) -> int:

        @functools.lru_cache(maxsize=None)
        def rob_from(i):
            if i >= len(nums):
                return 0
            ans = max(rob_from(i + 1), nums[i] + rob_from(i + 2))
            return ans

        return rob_from(0)


nums = [1,2,3,1]  # 4
nums = [2,7,9,3,1]  # 12
print(Solution().rob(nums))


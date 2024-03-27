"""
House robber style?
"""

from typing import List
import collections


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:

        num_to_gain = collections.defaultdict(int)
        for i in range(len(nums)):
            num_to_gain[nums[i]] += nums[i]

        print(num_to_gain)

        @functools.lru_cache(maxsize=None)
        def dp(num):

            if num <= 0:
                return 0
            elif num == 1:
                return num_to_gain[num]

            return max(num_to_gain[num] + dp(num - 2), dp(num - 1))

        return dp(max(num_to_gain.keys()))

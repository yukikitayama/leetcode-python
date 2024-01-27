"""
num_to_total

dp(i)
  Base case
    If i == 0, return 0, nothing to add
    If i == 1, return num_to_total[1]

  return
    maximum points we can gain when we consider the numbers from 0 to i
    max(dp(i - 1), dp(i - 2) + num_to_total[i])

dp(max(nums)) covers the entire input
"""

from typing import List
import collections
import functools


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:

        num_to_total_point = collections.defaultdict(int)

        max_num = 0

        for num in nums:
            num_to_total_point[num] += num
            max_num = max(num, max_num)

        @functools.lru_cache(maxsize=None)
        def dp(i):

            if i == 0:
                return 0

            if i == 1:
                return num_to_total_point[i]

            return max(dp(i - 1), num_to_total_point[i] + dp(i - 2))

        return dp(max_num)



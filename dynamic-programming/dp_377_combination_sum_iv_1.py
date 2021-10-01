"""
- dp[i] represents the number of possible combination up it,
  - so dp[target] is the number to return
- base case, dp[0] is 1, to make 0, there's only one combinations of not choosing any num from nums
- initialize other dp with 0
- dp[1], with num 1, one combination, with num 2, no combination
- for each num in nums
  - dp[i] = dp[i] + dp[i - num]
    - num: 1, i: 1, dp[1] = dp[1] + dp[1 - 1] = 0 + 1 = 1
    - num: 1, i: 2, dp[2] = dp[2] + dp[2 - 1] = 0 + 1 = 1
    - But add combination from 2
    - num:2, i: 2, dp[2] = dp[2] + dp[2 - 2] = 1 + 1 = 2
"""


from typing import List
from functools import lru_cache


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:

        @lru_cache(maxsize=None)
        def combs(remain):
            if remain == 0:
                return 1

            result = 0

            for num in nums:

                if remain - num >= 0:
                    result += combs(remain - num)

            return result

        return combs(target)


nums = [1, 2, 3]
target = 4
print(Solution().combinationSum4(nums, target))


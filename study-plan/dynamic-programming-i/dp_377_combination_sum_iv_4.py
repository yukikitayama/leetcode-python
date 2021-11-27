"""
- dp[i] represents the number of combination to make i
- dp[0]: 1
- dp[1]: 1
- dp[2]: 2
- i: 3, (1, 1, 1), (1, 2), (2, 1), (3)
  - For 1, (11)+1, (2)+1, i - 1: 2, +=dp[2]
  - For 2, (1)+2, i - 2: 1, +=dp[1]
  - For 3, ()+3, i - 3: 0, +=dp[0]
  - dp[3] = dp[2] + dp[1] + dp[0] = 4
"""


from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:

        dp = [0] * (target + 1)
        dp[0] = 1

        for i in range(1, len(dp)):
            for num in nums:
                if i - num >= 0:
                    dp[i] += dp[i - num]

        return dp[-1]


nums = [1, 2, 3]
target = 4
print(Solution().combinationSum4(nums, target))





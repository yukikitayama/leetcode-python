"""
- Start: 8:34
- End: 8:36
- Saw solution: 1
- Optimized: 0
- Solved: 1


- Decide whether to rob the current house or not
- If rob the current, skip the next
- robFrom(i)
  - The robber has to maximize profit from i to n
  - robFrom(i) = max(robFrom(i + 1), nums[i] + robFrom(i + 2))
    - Current profit is a max of either
      - skip the current and rob the next
      - or rob the current, skip the next
"""


from typing import List


class Solution:
    def __init__(self):
        self.memo = {}

    def rob(self, nums: List[int]) -> int:
        return self.rob_from(0, nums)

    def rob_from(self, i, nums):
        # When an index goes beyond nums, it returns 0 profit
        # so it can safely avoid index out of bound error
        if i >= len(nums):
            return 0
        if i in self.memo:
            return self.memo[i]
        ans = max(self.rob_from(i + 1, nums), nums[i] + self.rob_from(i + 2, nums))
        self.memo[i] = ans
        return ans


nums = [1,2,3,1]  # 4
nums = [2,7,9,3,1]  # 12
print(Solution().rob(nums))


"""
Idea
- 1. decrease top 3
- 2. decrease top 2 and increase 1
- 3. decrease top 1 and increase 2
- 4. increase 3

Algorithm
- If length of nums is smaller than 5, return 0
- Otherwise,
  - Initialize ans to float('inf')
  - sort nums
  - for i in range(4)
    - take difference between
      - first and the fourth from the end
        - nums[len(nums) - (4 - i)] - nums[i]
        - ans = min(ans, the diff)
      - second and the 3rd from the end
        - nums[len(nums) - (4 - 1)] - nums[i]
        - ans = min(ans, the diff)
      - third

"""


from typing import List


class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) < 5:
            return 0

        nums.sort()

        ans = float('inf')
        for i in range(4):
            diff = nums[len(nums) - (4 - i)] - nums[i]
            ans = min(ans, diff)

        return ans


nums = [1, 5, 0, 10, 14]
nums = [6,6,0,1,1,4,6]
print(Solution().minDifference(nums))


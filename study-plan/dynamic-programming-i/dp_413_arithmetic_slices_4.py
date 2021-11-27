"""
- bottom up dynamic programming
- dp[i] represents the number of arithmetic slices in range (k, i),
  - k is the starting index that chain starts
  - dp[0] = 0
  - dp[1] = 0
  - dp[2] = ?
    - dp[2] = 1 if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]
  - dp[3]
    - if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]
      - dp[3] = 1 (length: 3) + dp[2] (length: 3) + 1 (length: 4)
        - How can I add extra one
- return sum(dp)
"""


from typing import List


# class Solution:
#     def numberOfArithmeticSlices(self, nums: List[int]) -> int:
#         dp = [0] * len(nums)
#
#         for i in range(2, len(nums)):
#             if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
#                 dp[i] = 1 + dp[i - 1] + dp[i]
#
#         # print(f'dp: {dp}')
#
#         # return dp[-1]
#         return sum(dp)


"""
Constant space
"""


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        dp = 0
        sum = 0
        for i in range(2, len(nums)):
            if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
                dp = 1 + dp
                sum += dp
            # Reset
            else:
                dp = 0

        return sum


nums = [1,2,3,4]
# nums = [1]
# nums = [1, 2, 3, 4, 5]  # 6
print(Solution().numberOfArithmeticSlices(nums))


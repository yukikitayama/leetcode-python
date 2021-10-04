"""
- dp[i] represents a boolean whether you can reach i from the first index
- Base case dp[0] is True
- Initialize max_so_far is 0
- for each index and num in nums from index of 0
  - if index <= max_so_far
    - max_so_far = max(max_so_far, index + nums)
    - if index <= max_so_far, dp[index] is True
"""


from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [False] * len(nums)
        dp[0] = True
        max_so_far = 0

        for i, num in enumerate(nums):
            if i <= max_so_far:
                max_so_far = max(max_so_far, num + i)
                dp[i] = True

            # print(f'i: {i}, num: {num}, max_so_far: {max_so_far}, dp: {dp}')

        return dp[-1]


nums = [2,3,1,1,4]
nums = [3,2,1,0,4]
print(Solution().canJump(nums))



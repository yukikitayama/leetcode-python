"""
- dp[i] represents the minimum number of jumps to reach index of i in nums
- Initialize all the elements in dp to len(nums) - 1
  because we can assume that we can always reach the last index
- dp[0] is 0 because of starting from first index
- dp[1] = dp[0] + 1 if (i - 1) + nums[i - 1] is equal to or bigger than i
- otherwise no change
- iterate index from 1 to len(nums) - 1
  - dp[i] = dp[i - 1]

- furthest = i + nums[i]

- steps: 0
- i: 0, nums[i]: 2, i + nums[i]: 2, steps: 1, dp[2]: 1
- i: 1, nums[i]: 3, i + nums[i]: 4, steps: 2, dp[4]: 2
- i: 2, nums[2]: 1, i + nums[i]: 3, steps: 3, dp[3]: 3
- i: 3, nums[3]: 1, i + nums[i]: 4, steps: 4, dp[4]: min(2, 4) = 2

- Initialize dp with 0 to len(nums) - 1
- for each index and num in nums
  - steps = i + 1
  - max_index = i + nums[i]
  - dp[max_index] = min(steps, dp[max_index])
- return dp[-1]

nums: [1, 2, 1, 1, 1]
dp:   [0, 1, 2, 2, 3]
i: 1, dp[i]: if nums[i - 1] + i - 1 >= i, dp[i]: dp[i - 1] + 1
"""


from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:

        # print(f'nums: {nums}')

        jumps = 0
        current_jump_end = 0
        farthest = 0

        for i in range(len(nums) - 1):

            farthest = max(farthest, i + nums[i])

            if i == current_jump_end:
                jumps += 1
                current_jump_end = farthest

            # print(f'  i: {i}, nums[i]: {nums[i]}, jumps: {jumps}, '
            #       f'current_jump_end: {current_jump_end}, farthest: {farthest}')

        return jumps


nums = [2, 3, 1, 1, 4]
nums = [2,3,0,1,4]
nums = [3, 2, 1]
nums = [1,2,1,1,1]
print(Solution().jump(nums))

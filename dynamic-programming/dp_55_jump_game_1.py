from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> int:

        # print(f'nums: {nums}')

        memo = [0] * len(nums)

        # Last element is goal, so it's good place
        memo[len(nums) - 1] = 1
        # print(f'len(memo): {len(memo)}, memo: {memo}')

        for i in range(len(nums) - 2, -1, -1):

            furthest_jump = min(i + nums[i], len(nums))

            # print(f'i: {i}, furthest_jump: {furthest_jump}')

            for j in range(i + 1, furthest_jump + 1):

                # print(f'j: {j}, memo: {memo}')

                if memo[j] == 1:
                    memo[i] = 1
                    break

        return memo[0] == 1




"""
2D dp array?
Start from the last index?
Make 1D dp array from the end?

0: unknow
-1: bad
1: good

Bottom-up dynamic programming with memoization
Time complexity
O(n^2)

Space complexity
O(n) for memo
"""

nums = [2,3,1,1,4]
nums = [3,2,1,0,4]
print(Solution().canJump(nums))

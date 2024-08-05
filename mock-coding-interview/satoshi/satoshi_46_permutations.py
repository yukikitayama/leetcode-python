"""
3! = 3 * 2 * 1 = 6

[1, 1, 2]
  [1(1), 1(2), 2]
  [1(2), 1(1), 2]

backtesting
"""

from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        ans = []

        # T O(MN),
        # N: 6, M: 21
        # nums: [0, 1, 2, 3, 4, 5]
        def backtesting(comb):

            # Terminate
            if len(comb) == len(nums):
                ans.append(comb[:])
                return

                # T: O(N) where N is length of nums
            for i in range(len(nums)):
                curr_num = nums[i]

                # M is length of comb, T: O(M)
                if curr_num not in comb:
                    comb.append(nums[i])
                    backtesting(comb)
                    # Backtrack
                    comb.pop()

        backtesting([])

        return ans

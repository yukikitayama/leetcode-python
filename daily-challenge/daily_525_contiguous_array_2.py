"""
[0, 1, 0, 0, 1, 1]

two pointers from left and right, move to center
"""

from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        balance = 0

        balance_to_index = {0: -1}
        ans = 0

        for i in range(len(nums)):

            if nums[i] == 0:
                balance -= 1

            elif nums[i] == 1:
                balance += 1

            if balance in balance_to_index:
                ans = max(i - balance_to_index[balance], ans)
            else:
                balance_to_index[balance] = i

            # print(f"i: {i}, balance: {balance}, balance_to_index: {balance_to_index}")

        return ans


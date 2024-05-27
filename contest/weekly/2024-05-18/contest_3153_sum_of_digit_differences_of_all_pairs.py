"""
T: O(N**2) doesn't work because nums length is 10**5 at worst case

"""

from typing import List


class Solution:
    def sumDigitDifferences(self, nums: List[int]) -> int:
        n = len(nums)
        m = len(str(nums[0]))

        # count is m by 10 2d matrix, m is index to ith digit in a num
        # 10: 0 to 9 digits
        count = [[0] * 10 for i in range(m)]

        # Number of total pairs for each digit position
        ans = n * (n - 1) // 2 * m
        for num in nums:
            for i, digit in enumerate(str(num)):

                # Decrement total pairs by the pairs created the previously counted and the current
                ans -= count[i][int(digit)]

                # Increment by the current to form a new pair to the next
                count[i][int(digit)] += 1

        # for row in count:
        #     print(row)

        return ans
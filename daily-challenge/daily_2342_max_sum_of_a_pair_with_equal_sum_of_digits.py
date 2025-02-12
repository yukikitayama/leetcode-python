"""
Hashmap
  k: 9, v: max val
  k: 7, v: max val
Descending sort nums
  [43, 36, 18, 13, 7]
  [0, 1, 2, 3, 4]
"""

from typing import List


class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        digit_sum_to_max_val = dict()
        ans = -1

        for num in nums:

            digit_sum = sum([int(digit) for digit in str(num)])

            if digit_sum in digit_sum_to_max_val:
                ans = max(ans, num + digit_sum_to_max_val[digit_sum])
                digit_sum_to_max_val[digit_sum] = max(digit_sum_to_max_val[digit_sum], num)

            else:
                digit_sum_to_max_val[digit_sum] = num

        return ans

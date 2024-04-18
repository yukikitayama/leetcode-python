"""
7 / 3 = 2.333

The smaller the divisor, the larger the sum
binary search
  left 1
  right threshold
  if sum is bigger than threshold
    search left
  if sum is smaller than threhold
    search right
  if sum is equal to threshold
    return ?

"""

from typing import List
import math


class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left = 1
        right = max(nums)
        while left <= right:
            mid = (left + right) // 2
            sum_ = 0
            for num in nums:
                sum_ += math.ceil(num / mid)

            print(f"mid: {mid}, sum_: {sum_}")

            # Sum is bigger, so we need to pick bigger divisor to make sum smaller
            if sum_ > threshold:
                left = mid + 1

            if sum_ < threshold:
                right = mid - 1

            # We could have smaller divisor to achieve the same result
            if sum_ == threshold:
                right = mid - 1

        return left
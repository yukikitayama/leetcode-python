"""
Compute prefix products as array
  [10, 5, 2, 6] ->
  [1, 10, 50, 100, 600]
To compute products in a subarray
  [5, 2, 6] -> 600 / 10
  [10, 5] -> 50 / 1
  [5, 2] -> 100 / 10
Two pointers to pick subarray?

Ans
  nums contain only positive numbers
  product of subarray is always increasing

  right - left + 1, this math can replace N^2 nested for loop to count up
  right - left + 1 will give you the number of counts, though it cannot give you exact combinations
  [1, 2, 3]
  left: 0, right: 0, r - l + 1 = 1, [1]
  left: 0, right: 1, r - l + 1 = 2, [1, 2], [2]
  left: 0, right: 2, r - l + 1 = 3, [1, 2, 3], [2, 3], [3]
  When incrementing right, computing right - left + 1 on the fly, and adding to answer can produce nested for loop count effect
"""

from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:

        # Edge: nums[i] >= 1, so less than 1 is impossible
        if k <= 1:
            return 0

        ans = 0

        prefix_product = 1
        left = 0

        for right in range(len(nums)):

            num = nums[right]

            prefix_product *= num

            # When violate
            while prefix_product >= k:
                # Dividing current prefix product by old number can remove the old number from the current prefix product
                prefix_product /= nums[left]
                left += 1

            # +1 for current element
            # Right - left gives us additional combination at current
            ans += right - left + 1

        return ans
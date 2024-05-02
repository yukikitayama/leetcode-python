"""
N, M, K
Time complexity: O(N)
Space complexity: O(1)

Hashmap
  k: number in nums
  v: index

30,000

300,000,000

O(N**2)

100,
O(N**2) = 10,000
"""

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 0

        num = None
        count = 0

        for right in range(len(nums)):

            if nums[right] != num:
                num = nums[right]
                count = 1

                nums[left] = nums[right]
                left += 1

            else:
                count += 1

                if count <= 2:
                    nums[left] = nums[right]
                    left += 1

        return left

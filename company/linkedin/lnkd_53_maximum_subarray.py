"""
- Use two pointers
- Whenever the sum of the array is negative, the entire array is not worth keeping,
  so reset it back to empty
-
"""


from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_subarray = nums[0]
        max_subarray = nums[0]

        for i in range(1, len(nums)):
            curr = nums[i]

            current_subarray += curr

            if current_subarray < curr:
                current_subarray = curr

            max_subarray = max(max_subarray, current_subarray)

        return max_subarray




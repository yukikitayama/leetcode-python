"""
23 % 6 = 5
25 % 6 = 1
29 % 6 = 5
29 + 6 = 35
[23, 25, 29, 35, 41]
"""

from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if len(nums) < 2:
            return False

        prefix_sum = 0
        remainder_to_index = {prefix_sum % k: -1}

        for i in range(len(nums)):

            prefix_sum += nums[i]

            # If exist, don't update, to make length longer
            if prefix_sum % k in remainder_to_index:
                if i - remainder_to_index[prefix_sum % k] >= 2:
                    return True

            else:
                remainder_to_index[prefix_sum % k] = i

        return False

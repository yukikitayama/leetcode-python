"""
- Time is O(n) by using two pointers
"""


from typing import List
import math
import bisect


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0

        prod = 1

        ans = left = 0

        for right, val in enumerate(nums):
            prod *= val

            # Product exceeds k, so move left pointer to reduce the product
            while prod >= k:
                prod /= nums[left]
                left += 1

            print(f'  left: {left}, right: {right}, right - left + 1: {right - left + 1}')

            ans += right - left + 1

        return ans


"""
left: 0, right: 0, [10]
left: 0, right: 1, [10, 5], [5]
left: 1, right: 2, [5, 2], [2]
left: 1, right: 3, [5, 2, 6], [2, 6], [6]
"""
nums = [10,5,2,6]
k = 100
print(Solution().numSubarrayProductLessThanK(nums, k))


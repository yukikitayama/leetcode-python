"""
"""


from typing import List


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        min1 = min2 = float('inf')
        max1 = max2 = max3 = float('-inf')

        for num in nums:

            if num <= min1:
                min1, min2 = num, min1
            elif num <= min2:
                min2 = num

            if num >= max1:
                max1, max2, max3 = num, max1, max2
            elif num >= max2:
                max2, max3 = num, max2
            elif num >= max3:
                max3 = num

        return max(
            max1 * min1 * min2,
            max1 * max2 * max3
        )


"""
Complexity
- Time is O(n) for one pass, optimized solution
- Space is O(1)
"""


nums = [1,2,3,4]
nums = [-1,-2,-3]
print(Solution().maximumProduct(nums))



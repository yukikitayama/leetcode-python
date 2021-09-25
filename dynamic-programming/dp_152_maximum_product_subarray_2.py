from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        max_so_far = nums[0]
        min_so_far = nums[0]
        result = max_so_far

        # print(f'result: {result}')

        for num in nums[1:]:

            # max_so_far, min_so_far = max(num, num * min_so_far, num * max_so_far), min(num, num * min_so_far, num * max_so_far)

            tmp = max_so_far
            max_so_far = max(num, num * min_so_far, num * tmp)
            min_so_far = min(num, num * min_so_far, num * tmp)
            result = max(max_so_far, result)

            # print(f'num: {num}, max_so_far: {max_so_far}, '
            #       f'min_so_far: {min_so_far}, result: {result}')

        return result

"""
num: -3, max: 12, min: -4, result: 12
num: -2, max: max(-2, 12, -24) = 12, min: min(-2, 8, -24) = -24, result: 12

Dynamic programming, one pass, no memoization
Time: O(n) to iterate a for loop, Space: O(1) because of no memoization
"""


nums = [2, 3, -2, 4]
# nums = [-2,0,-1]
# nums = [0, 2]
nums = [-4,-3,-2]
print(Solution().maxProduct(nums))

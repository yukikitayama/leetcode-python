from typing import List


class Solution:
    def minDifference(self, nums: List[int]) -> int:
        nums.sort()
        # for a, b in zip(nums[:4], nums[-4:]):
        #     print(f'a: {a}, b: {b}, b - a: {b - a}')
        return min(b - a for a, b in zip(nums[:4], nums[-4:]))


"""
Because we are required to perform at most 3 times, 
we only have the following 4 cases to minimize difference between min and max

1. Decrease top 3 big numbers
2. Decrease top 2 big numbers and increase top 1 small number
3. Decrease top 1 big number and increase top 2 small numbers
4. Increase top 3 small numbers

After sorting the nums, the above cases correspond the following indices to get differences. 
And we just use the minimum difference out of 4 case.

1. when we decrease top 3 big numbers, nums: [1, 2, 3, 4, 5] => [1, 2, 2, 2, 2], 
difference is nums[len(nums) - 4] - nums[0]: nums[1] - nums[0] = 2 - 1 =1

Time and space complexity, O(nlogn) by n representing the length of nums
"""


nums = [1, 5, 6, 13, 14, 15, 16, 17]
nums = [5,3,2,4]
nums = [1,5,0,10,14]
print(Solution().minDifference(nums))

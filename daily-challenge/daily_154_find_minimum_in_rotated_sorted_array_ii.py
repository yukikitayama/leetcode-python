"""
- time needs to be less than O(n)
"""


from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1

        while high > low:

            pivot = low + (high - low) // 2

            print(f'  low: {low}, pivot: {pivot}, high: {high}')

            if nums[pivot] < nums[high]:
                high = pivot

            elif nums[pivot] > nums[high]:
                # If not +1, low pointer will get stuck at the index of the largest number
                low = pivot + 1

            else:
                # If not high - 1, high pointer skips the smallest number index
                # and it will continue searching in the wrong interval which does not contain the smallest number
                high = high - 1

        return nums[low]


# nums = [1,3,5]
nums = [2,2,2,0,1]
print(Solution().findMin(nums))


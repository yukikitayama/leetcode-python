"""
Permute nums
  Create num from list
  Compare
  If it's max,
    return min
    When nums is sorted in descending order
      Return nums in ascendingorder
  else
    next larger number

Swap


"""

from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def swap(i, j):
            nums[i], nums[j] = nums[j], nums[i]

        def reverse(start):
            end = len(nums) - 1
            while start < end:
                swap(start, end)
                start += 1
                end -= 1

        # Find the first going down element from the right
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        # Find the next largest element
        if i >= 0:
            j = len(nums) - 1

            # Iterate as long as nums in right is smaller than current num
            # It means next largest to current num can be found
            while nums[i] >= nums[j]:
                j -= 1

            swap(i, j)
            # Reverse right part
            reverse(i + 1)

        # When i is -1, given nums is the max number, so we need to get smallest by reverse
        else:
            reverse(i + 1)


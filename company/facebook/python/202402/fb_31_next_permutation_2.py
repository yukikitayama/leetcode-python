"""
[1, 3, 5, 4, 2, 1]
[1, 4, 5, 3, 2, 1]
[1, 4, 1, 2, 3, 5]

Iterate from right to left
  Find an index of first element which is smaller than previous
  Iterate from right to left again
    Find an index of next greater element
    swap those 2 indices
    reverse the right part
If in the first iteration,
  pointer less than 0 and couldn't find
  return reverse
"""

from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p1 = len(nums) - 2

        while p1 >= 0:
            if nums[p1] < nums[p1 + 1]:
                p2 = len(nums) - 1
                while nums[p1] >= nums[p2]:
                    p2 -= 1
                nums[p1], nums[p2] = nums[p2], nums[p1]
                temp = nums[p1 + 1:]
                temp.reverse()
                nums[p1 + 1:] = temp
                # print(f"p1: {p1}, p2: {p2}")
                break

            p1 -= 1

        if p1 < 0:
            nums.reverse()

"""
iterate nums
  if current is 0, swap with a non-zero from a subset in the right

T: O(N)

If not in-place
  iterate
    if 0
      append to 0 array
    if not 0
      append to non-zero arrya
  merge two array and return

Two pointers
  p1 move until 0
  p2 move until non-0

  if p1 is 0 and p2 is not 0
    swap

  move pointers

eg.
  [0, 1, 0, 3, 12]
  p1: 0, p2: 1
  swap
  [1, 0, 0, 3, 12]
  p1: 1, p2: 3
  swap
  [1, 3, 0, 0, 12]
  p1: 2, p2: 4


  [0, 0, 0, 0, 1]
"""

from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        prev = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[prev], nums[i] = nums[i], nums[prev]
                prev += 1
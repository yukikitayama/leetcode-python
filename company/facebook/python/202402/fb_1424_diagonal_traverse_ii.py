"""
Naive
  (0, 0)
  (1, 0), (0, 1)
  (2, 0), (1, 1), (0, 2)
  If square n by n
    (n - 1, 0), (n - 2, 1), (n - 3, 2)
  row decrement, col increments
  If non-square
    apply same row decrement and col increment
  If row sizes are different
    before accessing element
      check row index and col index are valid
        row always exists
        col checks if this row col index less than the length of the row
          if not, skip
  For each diagonal iteration, have a new list to append
    after iteration, extend the answer list with the current list

eg
[
    [14,12,19,16,9],
    [13,14,15,8,11],
    [11,13,1]
]

Append -1 to make each row complete
  Iteration is easier
"""

from typing import List
import collections


class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:

        diagonal_to_nums = collections.defaultdict(list)

        for r in range(len(nums) - 1, -1, -1):
            for c in range(len(nums[r])):
                diagonal = r + c
                diagonal_to_nums[diagonal].append(nums[r][c])

        ans = []
        curr = 0
        while curr in diagonal_to_nums:
            ans.extend(diagonal_to_nums[curr])
            curr += 1
        return ans


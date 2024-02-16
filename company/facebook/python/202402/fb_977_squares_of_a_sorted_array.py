"""
Naive
  Iterate each element and square
  Sort the squared array in ascending order
  T: O(NlogN)

T: O(N) approach
  two pointers, leftmost and rightmost, iterate towards center
  compare the absolute value
    bigger append to answer array from right
  reverse the answer array and return
"""

from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        ans = []

        left = 0
        right = len(nums) - 1

        while left <= right:

            left_num = nums[left] ** 2
            right_num = nums[right] ** 2

            if left_num > right_num:
                ans.append(left_num)
                left += 1

            else:
                ans.append(right_num)
                right -= 1

        ans.reverse()

        return ans

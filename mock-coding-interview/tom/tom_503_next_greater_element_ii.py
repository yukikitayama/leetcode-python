"""
answer array [-1] filled

iterate nums array
  each num will be start point, and circulr back
    i, increment, at end 0 i % len(nums)
  start number
    if current number > start, save answer
      answer[start] = bigger
      break

T: O(N^2)

Track maximum so far variable
"""

from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:

        answer = [-1] * len(nums)

        for i in range(len(nums)):

            num = nums[i]
            back = False
            j = i

            while not back:
                j = (j + 1) % len(nums)
                next_num = nums[j]
                if next_num > num:
                    answer[i] = next_num
                    back = True

                if j == i:
                    back = True

        return answer
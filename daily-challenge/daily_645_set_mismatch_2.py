"""
counter
for each number from 1 to n
  if counter value is 2, ans
  if number not in counter, ans
"""

import collections
from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        ans = [None] * 2

        counter = collections.Counter(nums)

        for i in range(1, len(nums) + 1):

            if i in counter.keys() and counter[i] == 2:
                ans[0] = i

            elif i not in counter.keys():
                ans[1] = i

        return ans

    def findErrorNums(self, nums: List[int]) -> List[int]:
        ans = [None] * 2

        for num in nums:

            if nums[abs(num) - 1] < 0:
                ans[0] = abs(num)

            else:
                # e.g. num: 2, index: 1 = 2 - 1
                nums[num - 1] *= -1

        for i in range(len(nums)):

            if nums[i] > 0:
                ans[1] = i + 1

        return ans




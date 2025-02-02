"""
Find start index
i % n
n length scan
  if goes down false
  otherwise true

if duplicate together
  first is start
if duplicate separate
  last is start
"""

from typing import List


class Solution:
    def check(self, nums: List[int]) -> bool:
        count = 0
        for i in range(1, len(nums)):
            if nums[i - 1] > nums[i]:
                count += 1

        if nums[-1] > nums[0]:
            count += 1

        return count <= 1

    def check1(self, nums: List[int]) -> bool:

        start = None
        min_so_far = float("inf")
        for i in range(len(nums)):
            if nums[i] < min_so_far:
                start = i
                min_so_far = nums[i]

        # Edge case
        if nums[0] == min_so_far and nums[-1] == min_so_far:
            start = len(nums) - 1

        curr = nums[start]
        for i in range(1, len(nums)):
            j = (start + i) % len(nums)
            if nums[j] < curr:
                return False
            curr = nums[j]
        return True


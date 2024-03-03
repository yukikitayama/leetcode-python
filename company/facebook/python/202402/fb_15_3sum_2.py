"""
sort
for each first number
  do two pointers at the right
    if sum is bigger than 0, decrement right
    if sum is smaller than 0, increment left
    if 0, append

Exclude duplicate
  if left is same as the previous left skip
"""

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()

        ans = []

        for i in range(len(nums)):

            # Avoid duplicate
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:

                sum_ = nums[i] + nums[left] + nums[right]

                if sum_ == 0:
                    ans.append([nums[i], nums[left], nums[right]])
                    # Explore different combination
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                elif sum_ > 0:
                    right -= 1

                elif sum_ < 0:
                    left += 1

        return ans

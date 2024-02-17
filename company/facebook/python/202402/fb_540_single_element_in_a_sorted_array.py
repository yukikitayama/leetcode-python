"""
Find an element such that
  left number is not same as current element AND right number is not same as current element
  if appears twice, either left number or right number is same as the current number
Even if doing binary search, it doesn't know which way to go

nums length is always odd


left is min number from nums
right is maxi number from nums
then search the mid number which has different numbers at both left and right


"""

from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:

        left = 0
        right = len(nums) - 1

        while left < right:

            # Take left one if even length
            mid = left + (right - left) // 2

            right_half_even = (right - mid) % 2 == 0

            # If the pair is at the right side
            if nums[mid] == nums[mid + 1]:
                if right_half_even:
                    left = mid + 2
                else:
                    right = mid - 1

            # If the pair is at the left side
            elif nums[mid - 1] == nums[mid]:
                if right_half_even:
                    right = mid - 2
                else:
                    left = mid + 1

            else:
                return nums[mid]

        return nums[left]


"""
- Requiring O(logn) time and O(1) space,
  - Binary search
- The array must be odd length if it contains a pair of numbers except single one number
  - Do binary search, find the mid number is not single number, remove the pair from the array
  - We are leaft with left subarray and right subarray
  - We know which direction to go, because
    - Odd length subsrray is the one which contains a single number
"""


from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        # < assures no index out of bound
        while left < right:
            mid = left + (right - left) // 2

            # e.g. right: 8, mid: 4, 8 - 4: 4
            # right - mid give us the length of subarray elements from at mid+1 to at right
            halves_are_even = (right - mid) % 2 == 0

            if nums[mid + 1] == nums[mid]:

                # mid's partner is to the right, and halves are even
                # right half becomes odd by removing mid numbers, so single number is to right
                if halves_are_even:
                    left = mid + 2

                # otherwise single number is to left, and left half does not contain mid numbers
                else:
                    right = mid - 1

            elif nums[mid - 1] == nums[mid]:

                # mid's partner is to the left, and halves are even,
                # left half becomes odd by removing mid numbers, so single number is to left
                if halves_are_even:
                    right = mid - 2
                else:
                    left = mid + 1

            else:

                return nums[mid]

        return nums[left]



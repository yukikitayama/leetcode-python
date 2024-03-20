"""
2 binary search to find left insert point and right insert point
Edge case
  not found target
"""

from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def binary_search(is_first):
            left = 0
            right = len(nums) - 1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] == target:

                    if is_first:
                        # Leftmost or in the middle
                        if mid == left or nums[mid - 1] != target:
                            return mid

                        right = mid - 1

                    else:

                        if mid == right or nums[mid + 1] != target:
                            return mid

                        left = mid + 1

                elif nums[mid] < target:
                    left = mid + 1

                elif nums[mid] > target:
                    right = mid - 1

            return -1

        first_index = binary_search(True)

        if first_index == -1:
            return [-1, -1]

        last_index = binary_search(False)

        return [first_index, last_index]

    def searchRange1(self, nums: List[int], target: int) -> List[int]:

        # Edge
        if not nums:
            return [-1, -1]

        def binary_search(is_left):
            left = 0
            right = len(nums) - 1
            while left <= right:
                mid = (left + right) // 2

                if is_left:
                    if nums[mid] < target:
                        left = mid + 1
                    elif nums[mid] >= target:
                        right = mid - 1

                else:
                    if nums[mid] <= target:
                        left = mid + 1
                    elif nums[mid] > target:
                        right = mid - 1

            if is_left and left < len(nums) and nums[left] == target:
                return left
            elif not is_left and right < len(nums) and nums[right] == target:
                return right
            else:
                return -1

        # print(binary_search(True))
        # print(binary_search(False))

        return [binary_search(True), binary_search(False)]


from typing import List


class BinarySearch:
    """
    binary_search_1 is the most basic and elementary form.
    """
    def binary_search_1(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1

        left = 0
        right = len(nums) - 1

        # End condition: left > right
        while left <= right:

            mid = (right + left) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1

    def binary_search_2(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1

        left = 0
        right = len(nums)

        # End condition: left == right
        while left < right:

            mid = (right + left) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid

        if left != len(nums) and nums[left] == target:
            return left
        else:
            return -1

    def binary_search_3(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1

        left = 0
        right = len(nums) - 1

        # End condition: left + 1 == right
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid
            else:
                right = mid

        if nums[left] == target:
            return left
        if nums[right] == target:
            return right
        return -1

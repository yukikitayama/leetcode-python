from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def reverse(nums, left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        reverse(nums, 0, len(nums) - 1)
        reverse(nums, 0, k % len(nums) - 1)
        reverse(nums, k % len(nums), len(nums) - 1)
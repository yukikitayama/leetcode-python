from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)

        # k could be bigger than length of nums,
        # so k = k % n to make k smaller than n
        k %= n

        # Reverse the entire array
        # [1, 2, 3, 4, 5] -> [5, 4, 3, 2, 1]
        self.reverse(nums, 0, n - 1)
        # Reverse the first part
        # k: 3, [5, 4, 3, 2, 1] -> [3, 4, 5, 2, 1]
        self.reverse(nums, 0, k - 1)
        # Reverse the second part
        # k: 3, [3, 4, 5, 1, 2]
        self.reverse(nums, k, n - 1)

    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start, end = start + 1, end - 1


"""
Time: O(2n) = O(n)
Space: O(1) because of no extra array
"""
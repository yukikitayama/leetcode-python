from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        count = 0
        start = 0

        while count < len(nums):

            i = start
            prev = nums[start]

            while True:

                next_i = (i + k) % len(nums)

                nums[next_i], prev = prev, nums[next_i]

                # temp = nums[next_i]
                # nums[next_i] = prev
                # prev = temp

                i = next_i
                count += 1

                if i == start:
                    break

            start += 1


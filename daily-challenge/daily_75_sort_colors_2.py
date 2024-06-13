from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """Three pointers"""
        p0 = 0
        p2 = len(nums) - 1
        i = 0

        while i <= p2:

            if nums[i] == 2:
                nums[i], nums[p2] = nums[p2], nums[i]
                p2 -= 1
                # Don't increment i
                # num: [1, 2, 0], swap 2 and 0 first, then stay the same position
                # then swap 0 and 1

            elif nums[i] == 0:
                nums[i], nums[p0] = nums[p0], nums[i]
                p0 += 1
                i += 1

            else:
                i += 1

        # print(nums)

    def sortColors1(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # Counting sort
        count = [0] * 4
        for num in nums:
            count[num] += 1

        i = 0
        for num in range(len(count)):
            while count[num] > 0:
                nums[i] = num
                i += 1
                count[num] -= 1

        # print(nums)

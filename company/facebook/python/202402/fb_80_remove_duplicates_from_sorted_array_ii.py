from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        curr_num = None
        curr_counter = 0
        left = 0

        for right in range(len(nums)):

            if nums[right] != curr_num:
                nums[left] = nums[right]

                curr_num = nums[right]
                curr_counter = 1

                left += 1

            elif nums[right] == curr_num and curr_counter < 2:
                nums[left] = nums[right]

                curr_counter += 1

                left += 1

        return left


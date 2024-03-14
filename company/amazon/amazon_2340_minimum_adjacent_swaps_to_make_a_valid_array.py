from typing import List


class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:

        # Edge
        if len(nums) == 1:
            return 0

        max_num = max(nums)
        min_num = min(nums)

        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == max_num:
                max_index = i
                break

        for i in range(len(nums)):
            if nums[i] == min_num:
                min_index = i
                break

        # print(f"min_num: {min_num}, min_index: {min_index}")
        # print(f"max_num: {max_num}, max_index: {max_index}")

        if min_index < max_index:
            return min_index + (len(nums) - max_index - 1)
        else:
            # -1 for intersect
            return min_index + (len(nums) - max_index - 1) - 1
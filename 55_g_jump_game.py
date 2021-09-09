from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last_position = len(nums) - 1
        # print(f'Last position: {last_position}')

        for i in range(last_position, -1, -1):
            if i + nums[i] >= last_position:
                last_position = i
                # print(f'Last position: {last_position}')

        return last_position == 0


"""
Time complexity
Let n the length of the array. O(n) because of a single pass from right to left

Space complexity
O(1) because we don't use any extra memory
"""


nums = [2, 3, 1, 1, 4]
print(Solution().canJump(nums))

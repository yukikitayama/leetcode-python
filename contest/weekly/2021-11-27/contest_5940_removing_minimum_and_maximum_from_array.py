from typing import List


class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        min_num = min(nums)
        max_num = max(nums)

        print(f'min_num: {min_num}, max_num: {max_num}')

        while len(nums):
            min_index = nums.index(min_num)
            max_index = nums.index(max_num)

            min_left_distance = min_index
            min_right_distance = len(nums) - min_index - 1
            max_left_distance = max_index
            max_right_distance = len(nums) - max_index - 1



nums = [2,10,7,5,4,1,8,6]
print(Solution().minimumDeletions(nums))




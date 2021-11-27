from typing import List


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)

        down = 1
        up = 1

        for i in range(1, len(nums)):

            if nums[i] > nums[i - 1]:
                up = down + 1
            elif nums[i] < nums[i - 1]:
                down = up + 1

        return max(down, up)


"""
up[i] is the longest wiggle subsequence length so far considering i th element as the ending element, ending with rising
down[i] is the longest wiggle subsequence length so far as the ending i th element, and ending with falling wiggle
"""
nums = [1,7,4,9,2,5]
nums = [1,17,5,10,13,15,10,5,16,8]
print(Solution().wiggleMaxLength(nums))


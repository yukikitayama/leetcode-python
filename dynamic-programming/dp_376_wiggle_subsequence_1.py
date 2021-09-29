from typing import List


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        # < 2 because 2 elements in length 2 array could have the same values, which is not wiggle
        if len(nums) < 2:
            return len(nums)

        up = [0] * len(nums)
        down = [0] * len(nums)

        # i is ending index incrementing
        for i in range(1, len(nums)):

            # print(f'i: {i}, up: {up}, down: {down}')

            # j is starting index bounded by i at the right side
            for j in range(i):

                # i: 1, j: 0,
                if nums[i] > nums[j]:
                    # If the current is rising, you can add 1 to down array, but you should not add 1 to up array
                    # because it's not wiggle
                    up[i] = max(up[i], down[j] + 1)

                elif nums[i] < nums[j]:
                    # Currently falling, so add 1 to up array, but no change to down array, because
                    # it keep increasing, and that's not wiggle
                    down[i] = max(down[i], up[j] + 1)

                # print(f'  j: {j}, up: {up}, down: {down}')

        # up and down arrays count from 2nd element in nums, so up[-1] and down[-1] are missing
        # one more element to get the length, so at last add 1
        return max(up[len(nums) - 1], down[len(nums) - 1]) + 1



"""
up[i] is the longest wiggle subsequence length so far considering i th element as the ending element, ending with rising
down[i] is the longest wiggle subsequence length so far as the ending i th element, and ending with falling wiggle
"""
nums = [1,7,4,9,2,5]
nums = [1,17,5,10,13,15,10,5,16,8]
print(Solution().wiggleMaxLength(nums))


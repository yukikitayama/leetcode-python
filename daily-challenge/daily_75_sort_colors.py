"""
- 3 pointers
"""


from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        left = 0
        right = len(nums) - 1
        curr = 0

        while curr <= right:
            if nums[curr] == 2:
                nums[right], nums[curr] = nums[curr], nums[right]
                right -= 1

                # You must not increment curr here, because
                # nums: [1, 2, 0] will end up [1, 0, 2]
                # After swapping 2 and 0, it needs to swap 0 and 1
                # curr += 1

            elif nums[curr] == 0:
                nums[left], nums[curr] = nums[curr], nums[left]
                left += 1
                curr += 1

            else:
                curr += 1

        print(nums)


nums = [2,0,2,1,1,0]
nums = [1, 2, 0]
print(Solution().sortColors(nums))
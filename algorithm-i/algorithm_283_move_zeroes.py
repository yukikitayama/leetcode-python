"""
- Initialize ans with the same size
- Initialize zero pointer to len(nums) - 1
- Initialize non-zero pointer to 0
- For each num in nums
  - if zero,
    - ans[zero pointer] = num,
    - decrement zero pointer
  - if non zero
    - ans[non zero pointer] = num
    - increment non zero pointer
- Time: O(n)
- Space: O(n)
"""


from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        last_non_zero_found_at = 0
        for cur in range(len(nums)):
            if nums[cur] != 0:
                nums[last_non_zero_found_at], nums[cur] = nums[cur], nums[last_non_zero_found_at]
                last_non_zero_found_at += 1

        # print(nums)


nums = [0,1,0,3,12]
print(Solution().moveZeroes(nums))

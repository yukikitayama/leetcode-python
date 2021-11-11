"""
- Prefix sum
- [-3, 2, -3, 4, 2]
  - [-3, -1, -4, 0, 2]
    - min: -4
- [1, 2]
  - [1, 3]
    - min: 1
- [1, -2, -3]
  - [1, -1, -4]
    - min: -4
- [1, -1]
  - [1, 0]
- If min negative
  - abs(min_num) + 1
- If min is positive
  - 1
- If min is 0
  - 1

Complexity
- Time O(n)
- Space is O(n)
"""


from typing import List


class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        # for i in range(1, len(nums)):
        #     nums[i] = nums[i] + nums[i - 1]
        #
        # if min(nums) < 0:
        #     return abs(min(nums)) + 1
        # else:
        #     return 1

        min_val = 0
        total = 0
        for num in nums:
            total += num
            min_val = min(min_val, total)
        return -min_val + 1


nums = [-3, 2, -3, 4, 2]
nums = [1,2]
nums = [1,-2,-3]
print(Solution().minStartValue(nums))


from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        for i in range(len(nums)):
            ans[i] = -1
            for j in range(1, len(nums)):
                if nums[(i + j) % len(nums)] > nums[i]:
                    ans[i] = nums[(i + j) % len(nums)]
                    break
        return ans

"""
Complexity
- Time is O(n^2)
"""


nums = [1, 2, 1]  # [2, -1, 2]
nums = [1,2,3,4,3]  # [2, 3, 4, -1, 4]
print(Solution().nextGreaterElements(nums))


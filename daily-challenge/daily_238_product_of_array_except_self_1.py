"""
Result
- Start: 9:29
- End: 9:37
- Saw solution: 1

Example 1
Input: nums = [1,2,3,4]
Output: [24,12,8,6]
- ans[0]: ans[1] * ans[2] * ans[3] = 2 * 3 * 4 = 24
- ans[1]: ans[0] * ans[2] * ans[3] = 1 * 3 * 4 = 12
- ans[2]: ans[0] * ans[1] * ans[3] = 1 * 2 * 4 = 8
- ans[3]: ans[0] * ans[1] * ans[2] = 1 * 2 * 3 = 6

Idea
- Left cumulative array
  - left[i] is the cumulative product from left to i - 1
- Right cumulative array
  - right[i] is the cumulative product from right to i + 1
- So take a product from left and right at the same index
  gives us the all the products except num at i

Input: nums = [1,2,3,4]
left: [1, 1, 2, 6]
right: [24, 12, 4, 1]
"""


from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        ans = [0] * n
        left = [0] * n
        right = [0] * n

        left[0] = 1
        for i in range(1, n):
            left[i] = left[i - 1] * nums[i - 1]

        right[n - 1] = 1
        for i in range(n - 2, -1, -1):
            right[i] = right[i + 1] * nums[i + 1]

        for i in range(n):
            ans[i] = left[i] * right[i]

        return ans


nums = [1,2,3,4]
# Output: [24,12,8,6]
nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]
print(Solution().productExceptSelf(nums))





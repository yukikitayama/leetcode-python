"""
nums: [1, 2, 3, 4]
1st iteration
ans: [1, 1, 2, 6]
3nd iteration
ans: [, ans[n - 3]: 1 * right: 12, ans[n - 2]: 2 * right: 4, ans[n-1]: 6 * right: 1]

ans: [24, 12, 8, 6]
"""


from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        ans = [0] * n

        ans[0] = 1
        for i in range(1, n):
            ans[i] = ans[i - 1] * nums[i - 1]

        right = 1
        for i in range(n - 1, -1, -1):
            ans[i] = right * ans[i]
            right *= nums[i]

        return ans


nums = [1,2,3,4]
# Output: [24,12,8,6]
nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]
nums = [1,2,3,4]
# [24,12,8,6]
print(Solution().productExceptSelf(nums))





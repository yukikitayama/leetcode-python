from typing import List


class Solution:
    def validSubarrays(self, nums: List[int]) -> int:
        ans = 0

        stack = []

        for i in range(len(nums)):

            while stack and nums[stack[-1]] > nums[i]:
                j = stack.pop()
                ans += i - j

            stack.append(i)

        while stack:
            j = stack.pop()
            ans += len(nums) - j

        return ans

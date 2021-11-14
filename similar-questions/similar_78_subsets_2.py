"""
- Similar to 1286
- Backtracking
"""


from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def backtracking(first, curr, k):
            if len(curr) == k:
                ans.append(curr[:])
                return

            for i in range(first, len(nums)):
                curr.append(nums[i])
                backtracking(i + 1, curr, k)
                curr.pop()

        for k in range(len(nums) + 1):
            backtracking(0, [], k)

        return ans


nums = [1, 2, 3]
print(Solution().subsets(nums))


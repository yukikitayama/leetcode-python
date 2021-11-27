from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        ans = []
        nums_twice = nums[:] + nums[:]
        for i in range(len(nums)):

            j = 0
            while i + j < len(nums_twice):

                curr = nums_twice[i + j]
                if curr > nums[i]:
                    ans.append(curr)
                    break
                j += 1

            if i + j == len(nums_twice):
                ans.append(-1)
        return ans


"""
Complexity
- Time is O(n^2)
"""


nums = [1, 2, 1]  # [2, -1, 2]
nums = [1,2,3,4,3]  # [2, 3, 4, -1, 4]
print(Solution().nextGreaterElements(nums))


from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        stack = []
        # From right to left, 2 times
        for i in range(2 * len(nums) - 1, -1, -1):

            # Keep the top of the stack the bigger number index to right of the current index
            while stack and nums[stack[-1]] <= nums[i % len(nums)]:
                stack.pop()

            # If stack is empty, currently there's not bigger element to the right of the current
            if not stack:
                ans[i % len(nums)] = -1
            # If there's something in the stack, top is the bigger element than the current
            else:
                ans[i % len(nums)] = nums[stack[-1]]

            stack.append(i % len(nums))

        return ans


"""
Complexity
- Time is O(2n) = O(n)
- Space is O(n) for stack
"""


nums = [1, 2, 1]  # [2, -1, 2]
nums = [1,2,3,4,3]  # [2, 3, 4, -1, 4]
print(Solution().nextGreaterElements(nums))


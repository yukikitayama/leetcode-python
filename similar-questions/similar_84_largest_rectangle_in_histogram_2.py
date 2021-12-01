"""
- Similar to 85. Maximal Rectangle

- Stack
"""


from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [-1]
        ans = 0

        for i in range(len(heights)):

            while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
                current_height = heights[stack.pop()]
                current_width = i - stack[-1] - 1
                ans = max(ans, current_height * current_width)

            stack.append(i)

        # There could be some indices left in the stack after the iteration
        while stack[-1] != -1:
            current_height = heights[stack.pop()]
            current_width = len(heights) - stack[-1] - 1
            ans = max(ans, current_height * current_width)

        return ans


heights = [2,1,5,6,2,3]
print(Solution().largestRectangleArea(heights))



from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [-1]
        ans = 0

        for i in range(len(heights)):

            while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
                # pop
                current_height = heights[stack.pop()]
                current_width = i - stack[-1] - 1
                ans = max(ans, current_height * current_width)

            stack.append(i)

        while stack[-1] != -1:
            current_height = heights[stack.pop()]
            current_width = len(heights) - stack[-1] - 1
            ans = max(ans, current_height * current_width)

        return ans


if __name__ == '__main__':
    heights = [2, 1, 5, 6, 2, 3]
    print(Solution().largestRectangleArea(heights))
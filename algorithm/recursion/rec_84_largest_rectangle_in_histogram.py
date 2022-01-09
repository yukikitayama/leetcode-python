from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [-1]
        ans = 0

        for i in range(len(heights)):

            while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:

                curr_height = heights[stack.pop()]
                curr_width = i - stack[-1] - 1
                ans = max(ans, curr_height * curr_width)

            stack.append(i)

        while stack[-1] != -1:
            curr_height = heights[stack.pop()]
            curr_width = len(heights) - stack[-1] - 1
            ans = max(ans, curr_height * curr_width)

        return ans


class Solution1:
    def largestRectangleArea(self, heights: List[int]) -> int:

        def calculate_area(heights: List[int], start: int, end: int) -> int:

            # Base case
            if start > end:
                return 0

            min_index = start
            for i in range(start, end + 1):
                # Update
                if heights[i] < heights[min_index]:
                    min_index = i

            # Divide and combine
            return max(
                heights[min_index] * (end - start + 1),
                calculate_area(heights, start, min_index - 1),
                calculate_area(heights, min_index + 1, end)
            )

        return calculate_area(heights, 0, len(heights) - 1)


if __name__ == '__main__':
    heights = [2, 1, 5, 6, 2, 3]
    print(Solution().largestRectangleArea(heights))

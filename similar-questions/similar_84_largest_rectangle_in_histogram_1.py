"""
- Similar to 85. Maximal Rectangle

- Brute force, better, two pointers
- TLE
"""


from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ans = 0
        for i in range(len(heights)):
            min_height = float('inf')
            for j in range(i, len(heights)):
                min_height = min(min_height, heights[j])
                ans = max(ans, min_height * (j - i + 1))
        return ans


heights = [2,1,5,6,2,3]
print(Solution().largestRectangleArea(heights))



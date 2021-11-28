from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left = 0
        right = len(height) - 1

        while left < right:

            area = min(height[left], height[right]) * (right - left)
            max_area = max(max_area, area)
            print(f'Max area: {max_area}')

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area


height = [1,8,6,2,5,4,8,3,7]
print(Solution().maxArea(height))

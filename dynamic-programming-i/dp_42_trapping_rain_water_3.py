"""
Algorithm
- scan from left to right
  - Track max height so far
- scan from right to left
  - Track max height so far
- Initialze ans to 0
- for each a bar height in height
  - ans += min(left max, right max) - a bar height
"""


from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        left_max = [0] * len(height)
        right_max = [0] * len(height)
        left_max_so_far = 0
        right_max_so_far = 0

        for i in range(len(height)):
            a_height = height[i]
            left_max_so_far = max(left_max_so_far, a_height)
            left_max[i] = left_max_so_far

        for i in range(len(height) - 1, -1, -1):
            a_height = height[i]
            right_max_so_far = max(right_max_so_far, a_height)
            right_max[i] = right_max_so_far

        # print(f'left_max:  {left_max}')
        # print(f'right_max: {right_max}')
        # print(f'height:    {height}')

        ans = 0

        for i in range(len(height)):
            ans += min(left_max[i], right_max[i]) - height[i]

        return ans


height = [0,1,0,2,1,0,1,3,2,1,2,1]
height = [4, 2, 0, 3, 2, 5]
print(Solution().trap(height))



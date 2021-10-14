from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 0:
            return 0

        size = len(height)
        left_max = [0] * len(height)
        right_max = [0] * len(height)

        # Base case
        left_max[0] = height[0]
        # DP
        for i in range(1, size):
            left_max[i] = max(height[i], left_max[i - 1])

        # Base case
        right_max[size - 1] = height[size - 1]
        # DP
        for i in range(size - 2, -1, -1):
            right_max[i] = max(height[i], right_max[i + 1])

        # Start at 1 and end at size - 1 because it does not have wall to trap water at the edges
        # - height[i] because there's not height * width are calculation, but because width is 1
        # in each position in height, it does the current entire area minus the occupied area by blocks
        # to get the area of trapped water
        ans = 0
        for i in range(1, size - 1):
            ans += min(left_max[i], right_max[i]) - height[i]

        return ans


"""
Time: O(n + n + n) = O(n) for 3 for loops
Space: O(n + n) = O(n) for 2 DP arrays
"""


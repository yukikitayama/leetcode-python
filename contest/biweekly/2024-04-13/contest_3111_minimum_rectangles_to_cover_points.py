"""
Sort by x
curr_left_x set by the first x
  keep iterating as long as difference between first x and curr x is within w
  if not
    increment answer
    update first x with the current x
"""

from typing import List


class Solution:
    def minRectanglesToCoverPoints(self, points: List[List[int]], w: int) -> int:
        ans = 0
        points.sort()
        prev = -1

        for i in range(len(points)):

            # Count opening
            if points[i][0] > prev:
                ans += 1
                prev = points[i][0] + w

        return ans

    def minRectanglesToCoverPoints1(self, points: List[List[int]], w: int) -> int:
        points.sort()
        ans = 0
        left_x = points[0][0]

        for i in range(1, len(points)):

            if points[i][0] - left_x <= w:
                continue

            else:
                ans += 1
                left_x = points[i][0]

        # Close last rectangle
        ans += 1

        return ans
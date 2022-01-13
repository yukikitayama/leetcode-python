"""
- greedy
- find overlap
- Delete point from the largest overlap
"""

from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])

        # print(f'points: {points}')

        end = points[0][1]
        ans = 1

        for i in range(1, len(points)):

            if points[i][0] > end:
                ans += 1
                end = points[i][1]

        return ans


if __name__ == '__main__':
    points = [[10, 16], [2, 8], [1, 6], [7, 12]]
    # 2
    points = [[1, 2], [3, 4], [5, 6], [7, 8]]
    # 4
    print(Solution().findMinArrowShots(points))

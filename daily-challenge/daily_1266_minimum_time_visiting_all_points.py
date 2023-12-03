from typing import List


class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:

        ans = 0

        for i in range(len(points) - 1):
            curr_x, curr_y = points[i]
            next_x, next_y = points[i + 1]

            ans += max(abs(curr_x - next_x), abs(curr_y - next_y))

        return ans



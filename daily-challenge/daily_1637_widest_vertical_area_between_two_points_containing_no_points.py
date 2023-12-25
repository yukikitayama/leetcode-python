from typing import List


class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()

        # print(points)

        ans = float("-inf")

        curr = points[0][0]

        for i in range(1, len(points)):

            diff = points[i][0] - curr

            ans = max(ans, diff)

            curr = points[i][0]

        return ans


if __name__ == "__main__":
    points = [[8, 7], [9, 9], [7, 4], [9, 7]]
    points = [[3, 1], [9, 0], [1, 0], [1, 4], [5, 3], [8, 8]]
    print(Solution().maxWidthOfVerticalArea(points))



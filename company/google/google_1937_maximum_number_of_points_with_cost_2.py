"""
- bottom up dp
- start from the first row and go down
- make 2d dp
- return the max of the last row of dp matrix
"""


from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:

        [print(row) for row in points]
        print()

        m = len(points)
        n = len(points[0])

        for i in range(m - 1):

            for j in range(n - 2, -1, -1):

                points[i][j] = max(points[i][j], points[i][j + 1] - 1)

            for j in range(n):

                points[i][j] = max(points[i][j], points[i][j - 1] - 1 if j else 0)

                points[i + 1][j] += points[i][j]

            [print(row) for row in points]
            print()

        return max(points[-1])



points = [[1,2,3],[1,5,1],[3,1,1]]
print(Solution().maxPoints(points))

"""
- bottom-up dp
"""


from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        if obstacleGrid[0][0] == 1:
            return 0
        else:
            obstacleGrid[0][0] = 1

        # [print(row) for row in obstacleGrid]

        # First row
        for i in range(1, len(obstacleGrid[0])):
            if obstacleGrid[0][i] != 1:
                obstacleGrid[0][i] = obstacleGrid[0][i - 1]
            elif obstacleGrid[0][i] == 1:
                obstacleGrid[0][i] = 0

        # First column
        for i in range(1, len(obstacleGrid)):
            if obstacleGrid[i][0] != 1:
                obstacleGrid[i][0] = obstacleGrid[i - 1][0]
            elif obstacleGrid[i][0] == 1:
                obstacleGrid[i][0] = 0

        # DP
        for row in range(1, len(obstacleGrid)):
            for col in range(1, len(obstacleGrid[0])):

                if obstacleGrid[row][col] == 0:
                    obstacleGrid[row][col] = obstacleGrid[row - 1][col] + obstacleGrid[row][col - 1]

                elif obstacleGrid[row][col] == 1:
                    obstacleGrid[row][col] = 0

        # print()
        # [print(row) for row in obstacleGrid]

        return obstacleGrid[len(obstacleGrid) - 1][len(obstacleGrid[0]) - 1]


if __name__ == '__main__':
    obstacleGrid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    # obstacleGrid = [[0, 1], [0, 0]]
    print(Solution().uniquePathsWithObstacles(obstacleGrid))

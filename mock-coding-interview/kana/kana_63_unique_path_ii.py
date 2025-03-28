from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
            return 0

        obstacleGrid[0][0] = 1

        for r in range(1, len(obstacleGrid)):
            obstacleGrid[r][0] = int(obstacleGrid[r][0] == 0 and obstacleGrid[r - 1][0] == 1)

        for c in range(1, len(obstacleGrid[0])):
            obstacleGrid[0][c] = int(obstacleGrid[0][c] == 0 and obstacleGrid[0][c - 1] == 1)

        for r in range(1, len(obstacleGrid)):
            for c in range(1, len(obstacleGrid[0])):
                if obstacleGrid[r][c] == 0:
                    obstacleGrid[r][c] = obstacleGrid[r - 1][c] + obstacleGrid[r][c - 1]
                else:
                    obstacleGrid[r][c] = 0

        for row in obstacleGrid:
            print(row)

        return obstacleGrid[-1][-1]

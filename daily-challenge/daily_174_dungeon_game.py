"""
-2    -3    3

-5    -10    1

10    30    -5

---
To dungeon


"""


from typing import List


class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:

        rows = len(dungeon)
        cols = len(dungeon[0])

        # dp[i][j] represents the minimum health to need at (i, j)
        dp = [[float('inf')] * cols for _ in range(rows)]

        # Base case
        if dungeon[rows - 1][cols - 1] < 0:
            dp[rows - 1][cols - 1] = -dungeon[rows - 1][cols - 1] + 1
        else:
            dp[rows - 1][cols - 1] = 1

        # print(f'dp: {dp}')

        def get_min_health(currCell, nextRow, nextCol):
            # If out of bound, it returns inf because we wanna know the minimum health,
            # so when getting answer, inf value will be excluded
            if nextRow >= rows or nextCol >= cols:
                return float('inf')

            nextCell = dp[nextRow][nextCol]

            # print(f'  nextCell: {nextCell}, currCell: {currCell}')

            # nextCell is the minimum health needed in the next dp cell
            # currCell is the health score that we can get at the current cell
            # If we have at least 1, we survive.
            # if currCell is bigger than nextCell, we have too much health, so get 1 by max()
            # if currCell is smaller than nextCell, the diff is the minimum health needed at current cell
            return max(1, nextCell - currCell)

        # for row in range(rows - 1, -1, -1):
        for row in reversed(range(rows)):

            # for col in range(cols - 1, -1, -1):
            for col in reversed(range(cols)):

                # print(f'row: {row}, col: {col}')

                curr_cell = dungeon[row][col]

                right_health = get_min_health(curr_cell, row, col + 1)
                down_health = get_min_health(curr_cell, row + 1, col)
                next_health = min(right_health, down_health)

                # If not out of bound, and not goal, update minimum health needed
                if next_health != float('inf'):
                    min_health = next_health
                # Base case: down right destination minimum health
                else:
                    # print(f'  else')
                    # If curr_cell is >= 0, we won't die, so minimum health is down to 1
                    # If curr_cell is negative, we will die, so to survive with at lease health 1,
                    # 1 - (-heath) = 1 + health needed. e.g. curr_cell is -5, 1 - (-5) = 6
                    # we need health 6 to survive
                    min_health = 1 if curr_cell >= 0 else (1 - curr_cell)

                dp[row][col] = min_health

                # print(f'row: {row}, col: {col}, '
                #       f'right_health: {right_health}, down_health: {down_health}, '
                #       f'next_health: {next_health}, min_health: {min_health}')

                # if (row, col) in ((2, 2), (2, 1), (1, 2)):
                #     print(f'row: {row}, col: {col}, '
                #           f'right_health: {right_health}, down_health: {down_health}, '
                #           f'next_health: {next_health}, min_health: {min_health}')

        return dp[0][0]


dungeon = [[-2,-3,3],[-5,-10,1],[10,30,-5]]
print(Solution().calculateMinimumHP(dungeon))




from typing import List


class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m = len(grid)
        n = len(grid[0])

        def test(i):
            """
            i tracks the current column
            i can change by grid[j][i] because it returns 1 or -1, so
            it can redirect the i column to correct value
            """
            for j in range(m):
                i2 = i + grid[j][i]

                # If it hits the wall cannot go down
                # also if neighbor direction is not the same, ball cannot go down
                if i2 < 0 or i2 >= n or grid[j][i2] != grid[j][i]:
                    return -1

                # Check new column and in the next row in the next iteration
                i = i2

            return i

        return list(map(test, range(n)))



if __name__ == '__main__':
    grid = [[1, 1, 1, -1, -1], [1, 1, 1, -1, -1], [-1, -1, -1, 1, 1], [1, 1, 1, 1, -1], [-1, -1, -1, -1, -1]]
    print(Solution().findBall(grid))

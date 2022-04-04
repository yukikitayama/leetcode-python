from typing import List


class Solution:
    def removeOnes(self, grid: List[List[int]]) -> bool:
        row1 = grid[0]
        row1_inverted = [v ^ 1 for v in grid[0]]

        for i in range(len(grid)):

            if grid[i] != row1 and grid[i] != row1_inverted:
                return False

        return True


if __name__ == '__main__':
    grid = [[0,1,0],[1,0,1],[0,1,0]]
    print(Solution().removeOnes(grid))

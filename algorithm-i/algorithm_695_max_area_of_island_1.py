"""
- Initialize ans to 0
- Iterate each row
  - Iterate each column
    - If the current cell is 1
      - DFS
        - Initialize area to 0
        - Modify input matrix to 0 when visit
        - Visit if the neighbors are 1
        - Increment area each time
        - When no more cells to go, update ans with max ans and current area

Implementation
- Recursive approach
"""


from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        ans = 0

        def dfs(grid, row, col):
            if not (0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] == 1):
                return 0

            grid[row][col] = 0

            # +1 to add current cell to the area
            return (
                1
                + dfs(grid, row + 1, col)
                + dfs(grid, row - 1, col)
                + dfs(grid, row, col + 1)
                + dfs(grid, row, col - 1)
            )

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    area = dfs(grid, row, col)
                    ans = max(ans, area)

        return ans


grid = [
    [0,0,1,0,0,0,0,1,0,0,0,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,1,1,0,1,0,0,0,0,0,0,0,0],
    [0,1,0,0,1,1,0,0,1,0,1,0,0],
    [0,1,0,0,1,1,0,0,1,1,1,0,0],
    [0,0,0,0,0,0,0,0,0,0,1,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,0,0,0,0,0,0,1,1,0,0,0,0]
]
print(Solution().maxAreaOfIsland(grid))

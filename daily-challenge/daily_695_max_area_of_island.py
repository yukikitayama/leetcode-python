"""
- 2 nested for loop to find an entry to an island
- Once entering BFS,
  - Change 1 to 0 to avoid visiting again
"""


from typing import List
import collections


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    curr = 0
                    queue = collections.deque([(i, j)])
                    grid[i][j] = 0

                    while queue:

                        row_curr, col_curr = queue.popleft()
                        curr += 1

                        for offset_row, offset_col in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                            next_row = row_curr + offset_row
                            next_col = col_curr + offset_col
                            if 0 <= next_row < len(grid) and 0 <= next_col < len(grid[0]):
                                if grid[next_row][next_col] == 1:
                                    grid[next_row][next_col] = 0
                                    queue.append((next_row, next_col))

                    ans = max(ans, curr)

        return ans


class Solution1:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()

        def dfs(row, col):

            if not (
                0 <= row < len(grid)
                and 0 <= col < len(grid[0])
                and (row, col) not in visited
                and grid[row][col] == 1
            ):
                return 0

            else:
                visited.add((row, col))
                return 1 + dfs(row + 1, col) + dfs(row - 1, col) + dfs(row, col - 1) + dfs(row, col + 1)

        ans = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                ans = max(ans, dfs(i, j))

        return ans


if __name__ == '__main__':
    grid = [
        [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]
    ]
    # 6
    print(Solution().maxAreaOfIsland(grid))

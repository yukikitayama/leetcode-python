from typing import List
import collections


class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:

        def find_root():
            for i in range(len(grid)):
                for j in range(len(grid)):
                    if grid[i][j]:
                        return i, j

        # Get a start index of one island
        start_row, start_col = find_root()

        queue = collections.deque()

        def dfs(i, j):
            # Mark as visited
            grid[i][j] = -1
            queue.append((i, j))

            for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= x < len(grid) and 0 <= y < len(grid) and grid[x][y] == 1:
                    dfs(x, y)

        # Collect indices of island, and mark the land as visited
        # The other island is not yet visited
        dfs(start_row, start_col)

        # Find the second land
        # 0 because [1st _ 2nd] is one flip
        step = 0
        while queue:

            for _ in range(len(queue)):

                r, c = queue.popleft()

                for x, y in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                    if 0 <= x < len(grid) and 0 <= y < len(grid):

                        # Because we marked all the land of the first island as visited,
                        # if we see 1, it's the land of the second island
                        if grid[x][y] == 1:
                            return step

                        elif grid[x][y] == 0:
                            grid[x][y] = -1
                            queue.append((x, y))

            step += 1


if __name__ == '__main__':
    grid = [
        [1, 1, 1, 1, 1],
        [1, 0, 0, 0, 1],
        [1, 0, 1, 0, 1],
        [1, 0, 0, 0, 1],
        [1, 1, 1, 1, 1]
    ]
    grid = [[0, 1, 0], [0, 0, 0], [0, 0, 1]]
    print(Solution().shortestBridge(grid))

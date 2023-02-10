from typing import List
import collections


class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:

        visited = [[0] * len(grid[0]) for _ in range(len(grid))]

        queue = collections.deque()

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                visited[r][c] = grid[r][c]
                if grid[r][c] == 1:
                    queue.append((r, c))

        ans = -1

        while queue:

            for _ in range(len(queue)):

                row, col = queue.popleft()

                for offset_row, offset_col in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    next_row = row + offset_row
                    next_col = col + offset_col

                    if 0 <= next_row < len(grid) and 0 <= next_col < len(grid[0]) and visited[next_row][next_col] == 0:
                        visited[next_row][next_col] = 1
                        queue.append((next_row, next_col))

            ans += 1

        return -1 if ans == 0 else ans


if __name__ == "__main__":
    grid = [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
    print(Solution().maxDistance(grid))


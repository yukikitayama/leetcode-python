from typing import List
import collections


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:

        visited = [[False] * len(grid[0]) for _ in range(len(grid))]

        def bfs(r, c):

            queue = collections.deque()
            queue.append((r, c))
            visited[r][c] = True
            is_closed = True

            while queue:

                curr_r, curr_c = queue.popleft()

                for offset_r, offset_c in [(0, 1), (0, -1), (1, 0), (-1, 0)]:

                    next_r = curr_r + offset_r
                    next_c = curr_c + offset_c

                    # If the next cell is out of grid, the current cell is at the boundary, so it's not closed
                    if next_r < 0 or next_r == len(grid) or next_c < 0 or next_c == len(grid[0]):
                        is_closed = False

                    elif grid[next_r][next_c] == 0 and not visited[next_r][next_c]:
                        queue.append((next_r, next_c))
                        visited[next_r][next_c] = True

            return is_closed

        ans = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0 and not visited[r][c] and bfs(r, c):
                    ans += 1

        return ans


if __name__ == "__main__":
    grid = [[1, 1, 1, 1, 1, 1, 1, 0], [1, 0, 0, 0, 0, 1, 1, 0], [1, 0, 1, 0, 1, 1, 1, 0], [1, 0, 0, 0, 0, 1, 0, 1],
           [1, 1, 1, 1, 1, 1, 1, 0]]
    print(Solution().closedIsland(grid))



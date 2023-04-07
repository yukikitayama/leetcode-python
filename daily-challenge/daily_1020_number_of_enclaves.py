"""
Start BFS from all the cells at the boundary of the grid
mark visited

reiterate grid and count all the land cells which are not visited yet
those land cells are not visited because they are found to be not connected to boundary cells from the first iteration.

"""


from typing import List
import collections


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:

        row = len(grid)
        col = len(grid[0])
        visited = [[False] * col for _ in range(row)]

        def bfs(r, c):

            queue = collections.deque()
            queue.append((r, c))
            visited[r][c] = True

            while queue:
                curr_r, curr_c = queue.popleft()

                for offset_r, offset_c in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    next_r = curr_r + offset_r
                    next_c = curr_c + offset_c

                    # If out of grid
                    if next_r < 0 or next_r >= row or next_c < 0 or next_c >= col:
                        continue

                    # If land, and if not visited
                    elif grid[next_r][next_c] and not visited[next_r][next_c]:
                        queue.append((next_r, next_c))
                        visited[next_r][next_c] = True

            return

        for r in range(row):
            if grid[r][0] and not visited[r][0]:
                bfs(r, 0)
            if grid[r][col - 1] and not visited[r][col - 1]:
                bfs(r, col - 1)

        for c in range(col):
            if grid[0][c] and not visited[0][c]:
                bfs(0, c)
            if grid[row - 1][c] and not visited[row - 1][c]:
                bfs(row - 1, c)

        # print(visited)

        ans = 0
        for r in range(row):
            for c in range(col):
                if grid[r][c] and not visited[r][c]:
                    ans += 1

        return ans


if __name__ == "__main__":
    grid = [[0, 0, 0, 0], [1, 0, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]
    print(Solution().numEnclaves(grid))


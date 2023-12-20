"""
As long as there is equal number of points to the left and right of the meeting point,
the total distance is minimized
"""


from typing import List
import collections


class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        self.grid = grid
        self.m = len(grid)
        self.n = len(grid[0])

        ans = float("inf")

        for r in range(self.m):
            for c in range(self.n):
                d = self.search(r, c)
                ans = min(ans, d)

        return ans

    def search(self, row, col):
        queue = collections.deque()
        queue.append((row, col, 0))
        total = 0
        visited = [[False] * self.n for _ in range(self.m)]

        while queue:

            r, c, d = queue.popleft()

            if r < 0 or c < 0 or r >= self.m or c >= self.n or visited[r][c]:
                continue

            if self.grid[r][c]:
                total += d

            visited[r][c] = True

            queue.append((r - 1, c, d + 1))
            queue.append((r + 1, c, d + 1))
            queue.append((r, c - 1, d + 1))
            queue.append((r, c + 1, d + 1))

        return total


class SolutionOpt:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        rows = []
        cols = []

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    rows.append(r)
                    cols.append(c)

        # print(f"rows: {rows}")
        # print(f"cols: {cols}")

        # Row is already sorted because of the above for loop
        row_med = rows[len(rows) // 2]
        # Col isn't sorted because the above for loop iterate horizontally then vertically
        cols.sort()
        col_med = cols[len(cols) // 2]

        # print(f"Median row: {row_med}")
        # print(f"Median col: {col_med}")

        def total_distance_1d(indices, median_index):
            ans = 0
            for idx in indices:
                ans += abs(idx - median_index)
            return ans

        vertical_distances = total_distance_1d(rows, row_med)
        horizontal_distances = total_distance_1d(cols, col_med)

        # print(f"Vertical distances: {vertical_distances}")
        # print(f"Horizontal distances: {horizontal_distances}")

        return vertical_distances + horizontal_distances


if __name__ == "__main__":
    grid = [
        [1, 0, 0, 0, 1],
        [0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0]
    ]
    print(SolutionOpt().minTotalDistance(grid))

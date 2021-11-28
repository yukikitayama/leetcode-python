from typing import List


class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        rows = []
        cols = []

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    rows.append(r)
                    cols.append(c)

        row = rows[len(rows) // 2]
        cols.sort()
        col = cols[len(cols) // 2]
        return self.min_distance_id(rows, row) + self.min_distance_id(cols, col)

    def min_distance_id(self, points: List[int], origin: int) -> int:
        distance = 0
        for point in points:
            distance += abs(point - origin)
        return distance


grid = [[1, 0, 0, 0, 1], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0]]
grid = [[1, 1]]
print(Solution().minTotalDistance(grid))

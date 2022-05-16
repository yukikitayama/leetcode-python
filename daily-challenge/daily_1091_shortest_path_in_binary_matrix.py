"""
- bfs
- Single source shortest path, but no weight
"""


from typing import List
import collections


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        m = len(grid)
        n = len(grid[0])

        if grid[0][0] != 0 or grid[m - 1][n - 1] != 0:
            return -1

        # Queue: [(row, col, distance), ...]
        queue = collections.deque([(0, 0, 1)])
        visited = {(0, 0)}

        while queue:

            curr_row, curr_col, distance = queue.popleft()

            # print(f'curr_row: {curr_row}, curr_col: {curr_col}, distance: {distance}')

            if curr_row == m - 1 and curr_col == n - 1:
                return distance

            for offset_row, offset_col in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]:

                next_row = curr_row + offset_row
                next_col = curr_col + offset_col

                if 0 <= next_row < m and 0 <= next_col < n and grid[next_row][next_col] == 0:

                    if (next_row, next_col) not in visited:

                        visited.add((next_row, next_col))
                        queue.append((next_row, next_col, distance + 1))

        return -1


class Solution1:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        m = len(grid)
        n = len(grid[0])

        if grid[0][0] != 0 or grid[m - 1][n - 1] != 0:
            return -1

        queue = collections.deque([(0, 0)])
        grid[0][0] = 1

        while queue:

            curr_row, curr_col = queue.popleft()

            if curr_row == m - 1 and curr_col == n - 1:
                return grid[curr_row][curr_col]

            for offset_row, offset_col in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]:

                next_row = curr_row + offset_row
                next_col = curr_col + offset_col

                if 0 <= next_row < m and 0 <= next_col < n:

                    if grid[next_row][next_col] == 0:

                        grid[next_row][next_col] = grid[curr_row][curr_col] + 1
                        queue.append((next_row, next_col))

        return -1


if __name__ == '__main__':
    grid = [[0, 1], [1, 0]]
    # 2
    # grid = [
    #     [0, 0, 0],
    #     [1, 1, 0],
    #     [1, 1, 0]
    # ]
    # 4
    grid = [[1, 0, 0], [1, 1, 0], [1, 1, 0]]
    # -1
    print(Solution().shortestPathBinaryMatrix(grid))

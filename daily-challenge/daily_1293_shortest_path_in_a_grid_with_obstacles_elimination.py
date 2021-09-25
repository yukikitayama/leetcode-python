from typing import List
from collections import deque


class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        rows = len(grid)
        cols = len(grid[0])

        if k >= rows - 1 + cols - 1:
            return rows - 1 + cols - 1

        state = (0, 0, k)
        steps = 0
        queue = deque([(state, steps)])
        visited = set(state)

        while queue:

            (curr_row, curr_col, curr_k), steps = queue.popleft()

            if curr_row == rows - 1 and curr_col == cols - 1:
                return steps

            for next_row, next_col in [
                (curr_row + 1, curr_col),
                (curr_row - 1, curr_col),
                (curr_row, curr_col + 1),
                (curr_row, curr_col - 1)
            ]:
                if 0 <= next_row < rows and 0 <= next_col < cols:
                    next_k = curr_k - grid[next_row][next_col]
                    next_state = (next_row, next_col, next_k)

                    if next_k >= 0 and next_state not in visited:
                        queue.append((next_state, steps + 1))
                        visited.add(next_state)

        return -1

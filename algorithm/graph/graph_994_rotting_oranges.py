"""
Result
- Time: 14m
- Solved: 1
- Optimized: 1
- Saw solution: 0
"""


from typing import List
import collections


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = collections.deque()
        num_fresh_orange = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 2:
                    queue.append((row, col))
                elif grid[row][col] == 1:
                    num_fresh_orange += 1

        if not num_fresh_orange:
            return 0

        minute = -1

        while queue:

            minute += 1

            for _ in range(len(queue)):

                curr_row, curr_col = queue.popleft()

                for offset_row, offset_col in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    next_row = curr_row + offset_row
                    next_col = curr_col + offset_col

                    if 0 <= next_row < len(grid) and 0 <= next_col < len(grid[0]):
                        if grid[next_row][next_col] == 1:
                            grid[next_row][next_col] = 2
                            num_fresh_orange -= 1
                            queue.append((next_row, next_col))

        return minute if num_fresh_orange == 0 else -1


grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
grid = [[2,1,1],[0,1,1],[1,0,1]]
grid = [[0,2]]
grid = [[1]]
print(Solution().orangesRotting(grid))



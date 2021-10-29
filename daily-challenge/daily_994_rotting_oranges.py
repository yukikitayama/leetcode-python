"""
- Iterate each row and col
  - If current cell is 2 rotten orange
    - BFS
      - Backtrack or mark visited
  - If current cell is 1 fresh orange
    - Count the number of fresh orange
- Return minimum minute if fresh orange is 0
  - if fresh orange remains, return -1
"""


from typing import List
import collections


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = collections.deque()

        fresh_orange = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 2:
                    queue.append((row, col))
                if grid[row][col] == 1:
                    fresh_orange += 1

        # Mark the end of the current level in BFS
        queue.append((-1, -1))

        # Start from -1 because the first incrementation occurs when the first existing rotten orange finish
        # BFS pops the the first rotten orange and increment when it gets -1, but
        # rotten orange was already in the grid, so it doesn't make sense to increment for
        # for the first appearance of the rotten orange.
        minute = -1

        while queue:
            curr_row, curr_col = queue.popleft()

            # If current level ends
            if curr_row == -1:
                minute += 1

                # If it still has the next level, mark the end
                if queue:
                    queue.append((-1, -1))

            else:
                for offset_row, offset_col in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    next_row = curr_row + offset_row
                    next_col = curr_col + offset_col

                    if 0 <= next_row < len(grid) and 0 <= next_col < len(grid[0]):
                        if grid[next_row][next_col] == 1:
                            grid[next_row][next_col] = 2
                            queue.append((next_row, next_col))
                            fresh_orange -= 1

        print(f'fresh_orange: {fresh_orange}')

        return minute if fresh_orange == 0 else -1


grid = [[2,1,1],[1,1,0],[0,1,1]]
# grid = [
#     [2,1,1],
#     [0,1,1],
#     [1,0,1]
# ]
# grid = [[0,2]]
print(Solution().orangesRotting(grid))

"""
- If the current cell is 2, start BFS and return minimum distance
- before BFS, iterate all the cells to count the total number of oranges
- in BFS, count the number of oranges so far
- in BFS, when queue is empty, check if the oranges so far is the same as total oranges
  - if not return -1
"""


from typing import List
import collections


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = collections.deque()

        fresh_oranges = 0
        rows = len(grid)
        cols = len(grid[0])
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    queue.append((row, col))
                if grid[row][col] == 1:
                    fresh_oranges += 1

        # To count the minutes passed,
        # if the current level items in the queue are all popped out,
        # increment minute, so append(-1, -1) to indicate current level is over
        queue.append((-1, -1))

        # -1 because it increments minutes after indicator (-1, -1) is popped.
        # every level has indicator (-1, -1) at the end of the queue.
        # so the last level indicator popped out, and we increment again, but it didn't rot any orange
        # so at the end we increment one minute more, so we need to decrement it,
        # but rather start from -1, to omit decrementing at the end
        minutes = -1

        # print(f'before BFS: minutes: {minutes}, queue: {queue}')

        while queue:
            curr_row, curr_col = queue.popleft()

            if curr_row == -1:
                minutes += 1
                # If there's still rotten oranges remained in queue
                # add indicator to increment minutes
                if queue:
                    queue.append((-1, -1))

                # print(f'  current level done: minutes: {minutes}, queue: {queue}')

            else:
                for offset_row, offset_col in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                    next_row = curr_row + offset_row
                    next_col = curr_col + offset_col
                    if 0 <= next_row < rows and 0 <= next_col < cols:
                        if grid[next_row][next_col] == 1:
                            grid[next_row][next_col] = 2
                            fresh_oranges -= 1
                            queue.append((next_row, next_col))

        return minutes if fresh_oranges == 0 else -1


grid = [
    [2,1,1],
    [1,1,0],
    [0,1,1]
]
# grid = [
#     [2,1,1],
#     [0,1,1],
#     [1,0,1]
# ]
print(Solution().orangesRotting(grid))

